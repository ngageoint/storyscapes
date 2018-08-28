# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_cswrecordreference'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='cswrecord',
            options={
                'ordering': ['-modified', 'status', 'title'],
                'verbose_name': 'CSW Record',
                'verbose_name_plural': 'CSW Records'},
        ),
        migrations.AddField(
            model_name='cswrecord',
            name='status_message',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='cswrecordreference',
            name='record',
            field=models.ForeignKey(
                related_name='references', to='core.CSWRecord'),
        ),
        migrations.AlterField(
            model_name='cswrecordreference',
            name='scheme',
            field=models.CharField(
                max_length=100, verbose_name=b'Service Type',
                choices=[
                    (b'ESRI:AIMS--http-get-feature', b'MapServer'),
                    (b'ESRI:AIMS--http-get-feature', b'FeatureServer'),
                    (b'ESRI:AIMS--http-get-image', b'ImageServer'),
                    (b'WWW:LINK-1.0-http--json', b'JSON'),
                    (b'OGC:KML', b'KML'),
                    (b'WWW:LINK-1.0-http--rss', b'RSS'),
                    (b'WWW:DOWNLOAD', b'SHAPE'),
                    (b'WWW:LINK-1.0-http--soap', b'SOAP'),
                    (b'OGC:WCS', b'WCS'),
                    (b'OGC:WFS', b'WFS'),
                    (b'OGC:CS-W', b'CSW'),
                    (b'OGC:WMS', b'WMS'),
                    (b'OGC:WPS', b'WPS')]),
        ),
    ]
