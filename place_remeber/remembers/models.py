from django.contrib.gis.db import models

from users.models import User

class Remember(models.Model):
    name = models.CharField(max_length=30, verbose_name='Название')
    description = models.TextField(verbose_name='Описание')
    location = models.PointField(verbose_name='Локация')
    author = models.ForeignKey(
        User, 
        on_delete=models.CASCADE, 
        related_name='remember', 
        verbose_name='Автор'
    )
    created = models.DateTimeField(auto_now_add=True,)

    class Meta:
        ordering = ('-created',)
