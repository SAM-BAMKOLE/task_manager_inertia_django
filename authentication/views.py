from inertia import inertia
from django.shortcuts import redirect
from .forms import CustomUserCreationForm, CustomAuthenticationForm, CustomUserChangeFormInApp
from django.http import HttpRequest
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib import messages

def return_props(title, description, **kwargs):
    props = {
        "title": title,
        "description": description
        }
    for key, value in kwargs.items():
        props[key] = value

    return props

# Create your views here.
@inertia('auth/Register')
def register_page(request: HttpRequest):
    if request.user and request.user.is_authenticated:
        return redirect('task.dashboard')
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('authentication.login')
        
        errors = [error for errors in form.errors.values() for error in errors]
        return return_props('Register on TaskFlow', "Register a new account with TaskFlow", errors=errors)
    return return_props('Register on TaskFlow', "Register a new account with TaskFlow")
    
@inertia('auth/Login')
def login_page(request: HttpRequest):
    if request.user and request.user.is_authenticated:
        return redirect('task.dashboard')
    if request.method == "POST":
        form = CustomAuthenticationForm(request, data=request.POST)
        print()
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect(request.POST.get('next')) if request.POST.get('next') and len(request.POST.get('next')) > 0 else redirect('task.dashboard')
        errors = [error for errors in form.errors.values() for error in errors]
        return return_props('Login on TaskFlow', "Login to your TaskFlow account", errors=errors)
    props = {}
    if request.GET.get('next'):
        props['next'] = request.GET.get('next')
    return return_props('Login on TaskFlow', "Login to your TaskFlow account", **props)


def logout_page(request: HttpRequest):
    from django.contrib.auth import logout
    logout(request)
    return redirect('authentication.login')

@inertia('auth/ForgotPassword')
def forgot_password_page(request: HttpRequest):
    if request.method == "POST":
        email = request.POST.get('email')
        print(email)
        # Handle the password reset logic
        return return_props('Forgot Password', "Password reset link sent to your email", success="If an account with that email exists, a password reset link has been sent.")
    
@login_required
@inertia('auth/Profile')
def profile_page(request: HttpRequest):
    page_title = 'My Profile'
    page_description = 'View and edit your profile datails'

    from task.views import get_user_tasks_stats
    tasks_stats = get_user_tasks_stats(request)

    user = request.user
    if request.method == "POST" and request.POST.get('_method') == 'PUT':
        form = CustomUserChangeFormInApp(request.POST, instance=user)

        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully')
            return redirect('authentication.profile')
        return return_props(page_title, page_description, tasks_stats=tasks_stats, user=user, errors=form.errors)
    
    return return_props(page_title, page_description, tasks_stats=tasks_stats, user=user)

