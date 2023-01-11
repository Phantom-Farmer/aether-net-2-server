import datetime
from django.db import models
from .user import User
from .sleep_card import Sleep_Card

class Dream_Journal(models.Model):

    time_stamp = models.DateField(("Date"), default=datetime.date.today)
    sleep_review = models.CharField(max_length=500)
    dream = models.CharField(max_length=1000)
    sleep_number = models.ForeignKey(Sleep_Card, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
