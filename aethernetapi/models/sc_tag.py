from django.db import models
from .sleep_card import Sleep_Card
from .tag import Tag

class SC_Tag(models.Model):

    sleep_number = models.ForeignKey(Sleep_Card, on_delete=models.CASCADE)
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)
