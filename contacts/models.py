from django.db import models
from django.contrib.auth.models import AbstractUser

class Contacts(AbstractUser):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    telefone = models.CharField(max_length=30)
    created_at = models.DateTimeField(auto_now_add=True)

    client = models.ForeignKey(
        "clients.Client",
        on_delete=models.CASCADE,
        related_name="contacts",
    )