# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('teams', '0002_team_parent'),
    ]

    operations = [
        migrations.AlterField(
            model_name='membership',
            name='role',
            field=models.CharField(default=b'student', max_length=20, choices=[(b'manager', b'manager'), (b'owner', b'owner'), (b'teacher', b'teacher'), (b'student', b'student'), (b'assistant', b'assistant'), (b'assessor', b'assessor')]),
        ),
    ]
