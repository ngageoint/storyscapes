from __future__ import unicode_literals
from django.db import migrations, models
import exchange.themes.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Theme',
            fields=[
                ('id', models.AutoField(
                    verbose_name='ID',
                    serialize=False,
                    auto_created=True,
                    primary_key=True
                )),
                ('name', models.CharField(max_length=28)),
                ('description', models.CharField(max_length=64, blank=True)),
                ('default_theme', models.BooleanField(
                    default=False,
                    editable=False
                )),
                ('active_theme', models.BooleanField(default=False)),
                ('title', models.CharField(
                    default=None,
                    max_length=32,
                    null=True,
                    verbose_name=b'Landing Page Title',
                    blank=True
                )),
                ('tagline', models.CharField(
                    default=None,
                    max_length=64,
                    null=True,
                    verbose_name=b'Landing Page Tagline',
                    blank=True
                )),
                ('running_hex', exchange.themes.fields.ColorField(
                    default=b'0F1A2C',
                    max_length=7,
                    null=True,
                    verbose_name=b'Header Footer Color',
                    blank=True
                )),
                ('running_text_hex', exchange.themes.fields.ColorField(
                    default=b'FFFFFF',
                    max_length=7,
                    null=True,
                    verbose_name=b'Header Footer Text Color',
                    blank=True
                )),
                ('hyperlink_hex', exchange.themes.fields.ColorField(
                    default=b'0F1A2C',
                    max_length=7,
                    null=True,
                    verbose_name=b'Hyperlink Color',
                    blank=True
                )),
                ('pb_text', models.CharField(
                    default=b'Boundless Spatial',
                    max_length=32,
                    blank=True,
                    help_text=b'Text for the Powered by section in the footer',
                    null=True,
                    verbose_name=b'Footer Link Text'
                )),
                ('pb_link', models.URLField(
                    default=b'http://boundlessgeo.com/',
                    blank=True,
                    help_text=b'Link for the Powered by section in the footer',
                    null=True,
                    verbose_name=b'Footer Link URL'
                )),
                ('docs_link', models.URLField(
                    default=None,
                    blank=True,
                    help_text=b'Link for the Documentation',
                    null=True,
                    verbose_name=b'Documentation Link URL'
                )),
                ('docs_text', models.CharField(
                    default=b'Documentation',
                    max_length=32,
                    blank=True,
                    help_text=b'Text for the documentation link',
                    null=True,
                    verbose_name=b'Documentation Text'
                )),
                ('background_logo', models.ImageField(
                    default=None,
                    upload_to=b'theme/img/',
                    blank=True,
                    help_text=b'Note: will resize to 1440px (w)  350px (h)',
                    null=True,
                    verbose_name=b'Background Image'
                )),
                ('primary_logo', models.ImageField(
                    default=None,
                    upload_to=b'theme/img/',
                    blank=True,
                    help_text=b'Note: will resize to height 96px',
                    null=True,
                    verbose_name=b'Primary Logo'
                )),
                ('banner_logo', models.ImageField(
                    default=None,
                    upload_to=b'theme/img/',
                    blank=True,
                    help_text=b'Note: will resize to height 35px',
                    null=True,
                    verbose_name=b'Header Logo'
                )),
            ],
        ),
    ]
