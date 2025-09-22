from django.db import models

# Create your models here.
class Task(models.Model):
    class Priority_Level(models.TextChoices):
        LOW = 'LOW', 'Low'
        MEDIUM = 'MEDIUM', 'Medium'
        HIGH = 'HIGH', 'High'
    

    title = models.CharField(max_length=150)
    description = models.CharField(max_length=255)
    due_date = models.DateField()
    priority = models.CharField(max_length=6, choices=Priority_Level.choices, default=Priority_Level.MEDIUM)
    is_completed = models.BooleanField(default=False)
    owner = models.ForeignKey('authentication.User', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    tags = models.ManyToManyField('task.Tag', null=True)

    def __str__(self):
        return self.title
    

class Tag(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name