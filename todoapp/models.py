from django.db import models

# Create your models here.


class TodoItemModel(models.Model):
    title = models.CharField(max_length=100)
    is_completed = models.BooleanField(default=False)
    status = models.BooleanField(default=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.title