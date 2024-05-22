# Generated by Django 5.0.6 on 2024-05-22 11:24

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('remembers', '0002_remember_author'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='remember',
            options={'ordering': ('-created',)},
        ),
        migrations.AddField(
            model_name='remember',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]