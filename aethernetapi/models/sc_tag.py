from django.db import models
from .sleep_card import Sleep_Card
from .tag import Tag

class SC_Tag(models.Model):

    sleep_card = models.ForeignKey(Sleep_Card, on_delete=models.CASCADE)
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
