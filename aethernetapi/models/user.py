import datetime
from django.db import models


class User(models.Model):

    uid = models.CharField(max_length=50)
    image_url = models.URLField(max_length=250)
    email = models.EmailField(max_length=250)
    last_login = models.DateField(("Date"), default=datetime.date.today)
        