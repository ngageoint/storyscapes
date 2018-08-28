#
# Change the URL field from 200 to 512 character max length.
#

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('core', '0001_initial')
    ]

    operations = [
        migrations.AlterField(
            model_name='CSWRecord',
            name='source',
            field=models.URLField(max_length=512, blank=False),
        )
    ]
