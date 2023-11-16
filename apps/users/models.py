from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse


class User(AbstractUser):
    image = models.ImageField(upload_to="users", null=True)

    def get_absolute_url(self):
        return reverse("profile", args=[self.username])
