# from django.db import models
from django.contrib.gis.db import models

class Remember(models.Model):
    name = models.CharField(max_length=30, verbose_name='Название')
    description = models.TextField(verbose_name='Описание')
    location = models.PointField(verbose_name='Локация')
