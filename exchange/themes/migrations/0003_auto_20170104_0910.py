# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import exchange.themes.fields


class Migration(migrations.Migration):

    dependencies = [
        ('themes', '0002_auto_20160918_2121'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='theme',
            name='hyperlink_hex',
        ),
        migrations.AddField(
            model_name='theme',
            name='running_link_hex',
            field=exchange.themes.fields.ColorField(
                default=b'29748F', max_length=7, null=True,
                verbose_name=b'Header Footer Link Color', blank=True),
        ),
        migrations.AlterField(
            model_name='theme',
            name='background_logo',
            field=models.ImageField(
                default=None, upload_to=b'theme/img/', blank=True,
                help_text=b'Note: will resize to width 1440px and height '
                          b'350px',
                null=True, verbose_name=b'Background Image'),
        ),
        migrations.AlterField(
            model_name='theme',
            name='docs_text',
            field=models.CharField(
                default=b'Documentation', max_length=32, blank=True,
                help_text=b'Text for the documentation link',
                null=True, verbose_name=b'Footer Documentation Text'),
        ),
    ]
