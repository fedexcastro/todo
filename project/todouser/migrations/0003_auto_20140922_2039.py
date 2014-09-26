# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('todouser', '0002_auto_20140922_1504'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('age', models.PositiveIntegerField(null=True, blank=True)),
                ('country', models.CharField(max_length=55, null=True, blank=True)),
                ('state', models.CharField(max_length=55, null=True, blank=True)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='todouser',
            name='groups',
        ),
        migrations.RemoveField(
            model_name='todouser',
            name='user_permissions',
        ),
        migrations.DeleteModel(
            name='TodoUser',
        ),
    ]
