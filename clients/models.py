from django.db import models
from django.contrib.auth.models import AbstractUser

class Client(AbstractUser):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    telefone = models.CharField(max_length=30)
    created_at = models.DateTimeField(auto_now_add=True)

    user = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
        related_name="clients",
        null=True,
    )