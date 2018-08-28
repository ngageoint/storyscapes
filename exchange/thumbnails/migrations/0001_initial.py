#
# Create the thumbnail table in the database.
#

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = []

    operations = [
        migrations.CreateModel(
            name='Thumbnail',
            fields=[
                ('id', models.AutoField(
                    serialize=False, auto_created=True, primary_key=True)),
                ('object_type', models.CharField(max_length=255, blank=False)),
                ('object_id', models.CharField(max_length=255, blank=False)),
                ('thumbnail_mime', models.CharField(
                    max_length=127, null=True, blank=True)),
                ('thumbnail_img', models.BinaryField(null=True, blank=True)),
                ('is_automatic', models.BooleanField(default=True)),
            ]
        )
    ]
