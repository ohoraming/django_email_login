from django.db import models
from account.models import User

# Create your models here.

class Todo(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    todo_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=50)
    content = models.TextField()
    is_deleted = models.BooleanField(default=False)
    modified_at = models.DateTimeField(auto_now=True)
    create_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['create_at']