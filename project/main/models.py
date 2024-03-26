from django.db import models
from datetime import datetime

class Shop(models.Model):
    name = models.CharField(max_length=255, default='')
    img_url = models.CharField(max_length=255, default='')
    price = models.CharField(max_length=255, default='')
    description = models.TextField(default='')
    rating = models.CharField(max_length=255, default='')
    create_date = models.DateTimeField(default=datetime.now)
    object = models.CharField(max_length=255, default='')

    def __str__(self):
        return self.name