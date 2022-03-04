from django.db import models

# Create your models here.


class UserModel(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    photos = models.ImageField(upload_to='images')
    email = models.EmailField(max_length=100)
    status = models.BooleanField(default=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.email
