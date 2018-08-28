from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '24_to_26'),
        ('core', '0006_auto_20170531_1026'),
    ]

    def move_data(apps, schema_editor):
        CSWRecord = apps.get_model("core", "cswrecord")
        TopicCategory = apps.get_model("base", "topiccategory")

        for record in CSWRecord.objects.all():
            try:
                record.topic_category = TopicCategory.objects.filter(
                    identifier__iexact=record.category, is_choice=True)[0]
                record.save()
            except:
                pass

    operations = [
        migrations.AddField(
            model_name='cswrecord',
            name='topic_category',
            field=models.ForeignKey(
                blank=True, to='base.TopicCategory', null=True),
        ),
        migrations.AlterField(
            model_name='cswrecordreference',
            name='scheme',
            field=models.CharField(
                max_length=100, verbose_name=b'Service Type',
                choices=[
                    (b'ESRI:AIMS--http-get-map', b'MapServer'),
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
        migrations.RunPython(move_data),
    ]
