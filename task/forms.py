from django import forms
from task.models import Task

class TaskCreateForm(forms.ModelForm):
    # title = forms.CharField(max_length=150)
    # description = forms.CharField(max_length=255)
    # is_completed = forms.BooleanField(initial=False)
    # due_date = forms.DateField()
    # priority = forms.TypedChoiceField(choices=Task.Priority_Level.choices)

    class Meta:
        model = Task
        fields = ('title', 'description', 'is_completed', 'due_date', 'priority')

