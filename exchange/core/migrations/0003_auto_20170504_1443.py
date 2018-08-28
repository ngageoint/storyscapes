# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_lengthen_csw_source'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cswrecord',
            name='contact_information',
        ),
        migrations.AddField(
            model_name='cswrecord',
            name='contact_email',
            field=models.CharField(max_length=128, blank=True),
        ),
        migrations.AddField(
            model_name='cswrecord',
            name='contact_phone',
            field=models.CharField(max_length=128, blank=True),
        ),
        migrations.AlterField(
            model_name='cswrecord',
            name='creator',
            field=models.CharField(
                max_length=328, verbose_name=b'Agency', blank=True),
        ),
        migrations.AlterField(
            model_name='cswrecord',
            name='source',
            field=models.URLField(
                max_length=512, verbose_name=b'Service Endpoint'),
        ),
        migrations.AlterField(
            model_name='thumbnailimage',
            name='thumbnail_image',
            field=models.ImageField(
                upload_to=b'/vagrant/.storage/media/thumbs'),
        ),
    ]
