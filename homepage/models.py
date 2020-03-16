from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Info_user(models.Model):
    user_login = models.ForeignKey(User, on_delete=models.CASCADE)
    algoritm = models.TextField()
    date = models.DateTimeField(default=timezone.now)
