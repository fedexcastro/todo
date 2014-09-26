# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todouser', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todouser',
            name='age',
            field=models.PositiveIntegerField(null=True, blank=True),
        ),
    ]
