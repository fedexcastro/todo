from django.db import models
from django.contrib.auth.models import User
from tastypie.models import create_api_key


class TodoItem(models.Model):
    user = models.ForeignKey('auth.User', db_index=True)
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=500)
    priority = models.PositiveIntegerField()
    last_edit_datetime = models.DateTimeField(auto_now=True)
    created_datetime = models.DateTimeField(auto_now=True)
    due_date = models.DateTimeField(blank=True, null=True)
    completed = models.BooleanField(default=False)


models.signals.post_save.connect(create_api_key, sender=User)
