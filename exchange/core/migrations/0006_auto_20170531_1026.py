# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_auto_20170531_0642'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cswrecord',
            name='abstract',
            field=models.TextField(blank=True),
        ),
    ]
