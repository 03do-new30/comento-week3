from django.db import models

# Create your models here.
class Todo(models.Model):
    title = models.TextField(null=False, blank=False)
    description = models.TextField(null=False, blank=False)
    is_completed = models.BooleanField(default=False)
    created_at = models.DateField(auto_now_add = True)
    updated_at = models.DateField(auto_now = True)

class Comment(models.Model):
    todo_id = models.ForeignKey('Todo', related_name='comments', on_delete=models.CASCADE)
    contents = models.TextField(null=False, blank=False)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now = True)