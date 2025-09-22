from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404
from inertia import render, inertia, InertiaResponse
from .models import Task
from django.contrib.auth.decorators import login_required
from django.http.request import HttpRequest
from .forms import TaskCreateForm
from django.forms import model_to_dict
from datetime import date
from django.core.paginator import Paginator
from .models import Tag
from django.db.models import Q, Count
from django.contrib import messages


def return_props(title, description, **kwargs):
    return {
        "title": title,
        "description": description
        }

# Create your views here.
def home_page(request):
    page_title = 'Task Manager App'
    page_description = 'Create and manage your tasks'
    props = return_props(page_title, page_description)
    return render(request, 'Home', props)

@inertia('About')
def about_page(request):
    page_title = "About for task manager"
    page_description = "Description for about page - Task Manager"
    props = return_props(page_title, page_description)
    return props

@login_required
@inertia('Dashboard')
def dashboard_page(request: HttpRequest):
    page_title = 'Dashboard'
    page_description = 'Dashboard Description'
    props = return_props(page_title, page_description)

    tasks = get_user_tasks_stats(request)
    tasks['latest_tasks'] = Task.objects.filter(owner=request.user).order_by('-created_at')[:10]

    props['tasks_data'] = tasks
    props['name'] = request.user.first_name or request.user.email
    return props

@login_required
@inertia('task/Tasks')
def tasks_page(request: HttpRequest):
    page_title = 'Tasks'
    page_description = 'Tasks Description'
    props = return_props(page_title, page_description)
    filters = {}

    if request.GET.get('search') and request.GET.get('search') != 'ALL':
        filters['title__icontains'] = request.GET.get('search')
        # all_tasks = Task.objects.filter(owner=request.user, title__icontains=request.GET.get('search')).order_by('-created_at')
    if request.GET.get('status') and request.GET.get('status') != 'ALL':
        if request.GET.get('status') == 'OVERDUE':
            filters['due_date__lt'] = date.today()
        else:
            filters['is_completed'] = request.GET.get('status')
        # all_tasks = Task.objects.filter(owner=request.user, is_completed=request.GET.get('status')).order_by('-created_at')
    if request.GET.get('priority') and request.GET.get('priority') != 'ALL':
        filters['priority'] = request.GET.get('priority')
        # all_tasks = Task.objects.filter(owner=request.user, priority=request.GET.get('priority')).order_by('-created_at')
    # else:
    all_tasks = Task.objects.filter(owner=request.user, **filters).order_by('-created_at')
    paginator = Paginator(all_tasks, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    data = {
        'tasks': page_obj.object_list,
        'pagination': {
            'current_page': page_obj.number,
            'total_pages': paginator.num_pages,
            'has_previous': page_obj.has_previous(),
            'has_next': page_obj.has_next()
        }
    }
    props['page_obj'] = data
    return props

@login_required
@inertia('task/Create')
def task_create_page(request: HttpRequest):
    page_title = 'Taks Create'
    page_description = 'Taks Create Description'
    props = return_props(page_title, page_description)

    if request.method == "POST":
        form = TaskCreateForm(request.POST)
        inputed_tags = []
        for key, value in request.POST.items():
            if key.startswith('tags[') and key.endswith(']'):
                inputed_tags.append(value)
        if form.is_valid():
            task = form.save(commit=False)
            task.owner = request.user
            task.save()
            for item in inputed_tags:
                tag, created = Tag.objects.get_or_create(name=item)
                task.tags.add(tag)
            return redirect('task.dashboard')
        props['errors'] = form.errors
        # props['values'] = request.POST.items()
    return props

@login_required
@inertia('task/Edit')
def task_edit_page(request: HttpRequest, pk):
    page_title = 'Task Edit'
    page_description = 'Task Edit Description'
    props = return_props(page_title, page_description)
    task = get_object_or_404(Task, id=pk, owner=request.user)
    if request.method == 'POST' and request.POST.get('_method') == 'PUT':
        form = TaskCreateForm(request.POST, instance=task)
        # Deal with tags
        from .models import Tag
        inputed_tags = []
        for key, value in request.POST.items():
            if key.startswith('tags[') and key.endswith(']'):
                inputed_tags.append(value)
                
        if form.is_valid():
            task = form.save(commit=False)
            task.save()
            for item in inputed_tags:
                tag, created = Tag.objects.get_or_create(name=item)
                if tag not in task.tags.all():
                    task.tags.add(tag)
            
            messages.success(request, 'Task Edited Successfully')
            return redirect('task.edit', pk=task.id)
        props['errors'] = form.errors
        
    task = model_to_dict(task)
    props['task'] = task
    return props

@login_required
def task_update_completed(request: HttpRequest, pk):
    task = get_object_or_404(Task, id=pk, owner=request.user)
    if request.method == 'POST' and request.POST.get('_method') == 'PATCH':
        task.is_completed = not task.is_completed
        task.save()
        # http_referer = request.META.get('HTTP_REFEREF')
        # return redirect(http_referer if http_referer else 'task.dashboard')
    return InertiaResponse(request, None)

@login_required
def task_multiple_update_completed(request: HttpRequest):
    import json
    data: dict = json.loads(request.body)
    if request.method == 'POST' and data.get('_method') == 'PATCH':
        # tasks = get_list_or_404(Task, id__in=data.get('tasksIds'), owner=request.user)
        Task.objects.filter(id__in=data.get('tasksIds'), owner=request.user).update(is_completed=data.get('status'))

    return InertiaResponse(request, None)

@login_required
def task_delete(request: HttpRequest, pk):
    print(request.POST.get('_method'))
    if request.method == 'POST' and request.POST.get('_method') == 'DELETE':
        task = get_object_or_404(Task, id=pk, owner=request.user)
        task.delete()
        messages.info(request, 'Task Deleted Successfully')
        return InertiaResponse(request, None)

@login_required
@inertia('task/Tags')
def task_tags_page(request):
    page_title = 'Task Tags'
    page_description = 'Task Tags Description'
    props = return_props(page_title, page_description)
    user_tags = Tag.objects.annotate(task__count=Count('task', filter=Q(task__owner=request.user))).filter(task__count__gt=0)
    props['tags'] = user_tags.values('id', 'name', 'task__count')
    return props

@inertia('task/TagTasks')
def tag_tasks_page(request, pk):
    tag = get_object_or_404(Tag, id=pk)
    page_title = f'Tasks associated with - {tag.name}'
    page_description = f'All tags associated with {tag.name}'
    props = return_props(page_title, page_description)

    tasks = Task.objects.filter(owner=request.user, tags=tag).all()
    props['tasks'] = tasks
    return props

@inertia('task/Calendar')
def task_calendar_page(request):
    page_title = 'Task Calendar'
    page_description = 'Task Calendar Description'
    props = return_props(page_title, page_description)
    return props

# @inertia('Dashboard')
# def dashboard():
#     page_title = 'Dashboard'
#     page_description = 'Dashboard Description'
#     props = return_props(page_title, page_description)
#     return props



# ================== HELPER METHOD, NOT A ROUTE
def get_user_tasks_stats(request: HttpRequest):
    task_data = Task.objects.filter(owner=request.user).aggregate(
        total_count=Count('id'),
        completed_count=Count('id', filter=Q(is_completed=1)),
        overdue_count=Count('id', filter=Q(due_date__lt=date.today())) 
    )

    tasks = {}
    tasks['count'] = task_data['total_count']
    tasks['completed_count'] = task_data['completed_count']
    tasks['uncompleted_count'] = task_data['total_count'] - task_data['completed_count']
    tasks['overdue_count'] = task_data['overdue_count']

    return tasks