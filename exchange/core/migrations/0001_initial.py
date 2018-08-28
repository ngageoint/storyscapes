# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
import uuid
from django.conf import settings


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='CSWRecord',
            fields=[
                ('id', models.UUIDField(
                    default=uuid.uuid4, serialize=False,
                    editable=False, primary_key=True)),
                ('status', models.CharField(
                    default=b'Unknown', max_length=128)),
                ('classification', models.CharField(
                    max_length=128, blank=True)),
                ('title', models.CharField(max_length=328)),
                ('modified', models.DateField(default=datetime.date.today)),
                ('creator', models.CharField(max_length=328, blank=True)),
                ('record_type', models.CharField(max_length=128, blank=True)),
                ('alternative', models.CharField(max_length=128, blank=True)),
                ('abstract', models.TextField(blank=True)),
                ('source', models.URLField()),
                ('relation', models.CharField(max_length=128, blank=True)),
                ('record_format', models.CharField(
                    max_length=128, blank=True)),
                ('bbox_upper_corner', models.CharField(
                    default=b'85.0 180', max_length=128, blank=True)),
                ('bbox_lower_corner', models.CharField(
                    default=b'-85.0 -180', max_length=128, blank=True)),
                ('contact_information', models.CharField(
                    max_length=128, blank=True)),
                ('gold', models.BooleanField(default=False, max_length=128)),
                ('category', models.CharField(
                    blank=True, max_length=128,
                    choices=[(b'Air', b'Air (Aero)'),
                             (b'Intelligence', b'Intelligence'),
                             (b'Elevation', b'Elevation'),
                             (b'HumanGeog', b'Human Geography'),
                             (b'Basemaps', b'Basemaps'),
                             (b'Space', b'Space'), (b'Land', b'Land (Topo)'),
                             (b'Targeting', b'Targeting'),
                             (b'NamesBoundaries', b'Names & Boundaries'),
                             (b'MapsCharts', b'NGA Standard Maps & Charts'),
                             (b'Sea', b'Sea (Maritime)'),
                             (b'Imagery', b'Imagery/Collections'),
                             (b'Geomatics', b'Geodesy/Geodetics Geomatics'),
                             (b'Weather', b'Weather')])),
                ('user', models.ForeignKey(
                    related_name='csw_records_created',
                    to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
                'verbose_name': 'CSW Record',
                'verbose_name_plural': 'CSW Records',
            },
        ),
        migrations.CreateModel(
            name='ThumbnailImage',
            fields=[
                ('id', models.AutoField(
                    verbose_name='ID', serialize=False,
                    auto_created=True, primary_key=True)),
                ('thumbnail_image', models.ImageField(
                    upload_to=b'/scratch/media_root/thumbs')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
