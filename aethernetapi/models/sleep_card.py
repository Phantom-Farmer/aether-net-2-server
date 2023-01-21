import datetime
from django.db import models
from .user import User

class Sleep_Card(models.Model):

    time_stamp = models.DateField(("Date"), default=datetime.date.today)
    mind = models.CharField(max_length=500)
    body = models.CharField(max_length=500)
    meditation = models.CharField(max_length=50)
    favorite = models.BooleanField(default=False)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
