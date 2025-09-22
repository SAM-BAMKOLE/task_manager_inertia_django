from django.contrib import admin
from .models import Task, Tag

# Register your models here.
@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ("title", "description", "due_date", "is_completed")
    list_filter = ['title', 'due_date', 'is_completed']
    search_fields = ['title']

admin.site.register(Tag)