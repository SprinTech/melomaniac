from django.db import models

class User(models.Model):
    username = models.CharField(max_length= 100, null=False, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    email = models.EmailField(max_length=254, null=False, unique=True)
    password = models.CharField(max_length=254, null=False, unique=True)

    def __str__(self) -> str:
        return self.username