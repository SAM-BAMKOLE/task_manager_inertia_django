from django.urls import path
from .views import *

urlpatterns = [
    path('', home_page),
    path('about/', about_page),
    path('dashboard/', dashboard_page, name="task.dashboard"),
    path('task/', tasks_page, name="task.tasks"),
    path('task/create/', task_create_page, name="task.create"),
    path('task/calendar/', task_calendar_page, name="task.calendar"),
    path('task/tags/', task_tags_page, name="task.tags"),
    path('task/edit/<pk>', task_edit_page, name="task.edit"),
    path('task/update/multiple/', task_multiple_update_completed, name="task.update_multiple"),
    path('task/update/<pk>', task_update_completed, name="task.update_completed"),
    path('task/delete/<pk>', task_delete, name="task.delete"),
    path('task/tag/<pk>', tag_tasks_page, name='tag.tasks'),
]