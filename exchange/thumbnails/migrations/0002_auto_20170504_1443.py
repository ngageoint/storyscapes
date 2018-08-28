# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('thumbnails', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='thumbnail',
            name=b'id',
            field=models.AutoField(
                verbose_name='ID', serialize=False,
                auto_created=True, primary_key=True),
        ),
        migrations.AlterField(
            model_name='thumbnail',
            name=b'is_automatic',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterUniqueTogether(
            name='thumbnail',
            unique_together=set([('object_type', 'object_id')]),
        ),
    ]
