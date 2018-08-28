# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20170504_1443'),
    ]

    operations = [
        migrations.CreateModel(
            name='CSWRecordReference',
            fields=[
                ('id', models.AutoField(
                    verbose_name='ID', serialize=False,
                    auto_created=True, primary_key=True)),
                ('scheme',
                 models.CharField(
                     max_length=100, verbose_name=b'Service Type',
                     choices=[
                         (b'HTML', b'WWW:LINK-1.0-http--link'),
                         (b'ARCGISGPREST', b'ESRI:AIMS--http-get-feature'),
                         (b'ARCGISGPSOAP', b'ESRI:AIMS--http-get-feature'),
                         (b'ARCGISMAPREST', b'ESRI:AIMS--http-get-image'),
                         (b'ARCGISMAPSOAP', b'ESRI:AIMS--http-get-image'),
                         (b'ARCXML', b'ESRI:AIMS--http--configuration'),
                         (b'JSON', b'WWW:LINK-1.0-http--json'),
                         (b'KML', b'OGC:KML'),
                         (b'REST', b'WWW:LINK-1.0-http--rest'),
                         (b'RSS', b'WWW:LINK-1.0-http--rss'),
                         (b'SHAPE', b'WWW:DOWNLOAD'),
                         (b'SOAP', b'WWW:LINK-1.0-http--soap'),
                         (b'WCS', b'OGC:WCS'),
                         (b'WFS', b'OGC:WFS'),
                         (b'CS-W', b'OGC:CSW'),
                         (b'WMS', b'OGC:WMS'),
                         (b'WPS', b'OGC:WPS'),
                         (b'WIKI', b'WWW:LINK-1.0-http--link')])),
                ('url', models.URLField(max_length=512)),
                ('record', models.ForeignKey(to='core.CSWRecord')),
            ],
        ),
    ]
