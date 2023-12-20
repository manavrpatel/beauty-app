from uuid import uuid4
from django.db import models

class Service(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    name = models.CharField(max_length=40, unique=True, null=False)
    price = models.IntegerField(null=False)
    duration = models.IntegerField(null=False)

    def __str__(self):
        return self.name