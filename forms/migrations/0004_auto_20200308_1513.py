# Generated by Django 3.0.1 on 2020-03-08 09:43

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('forms', '0003_auto_20200307_1620'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='forms',
            new_name='gform',
        ),
    ]
