from __future__ import unicode_literals
from django.db import migrations


def load_themes(apps, schema_editor):
    Theme = apps.get_model("themes", "Theme")

    theme_storyscapes = Theme(
        name="StoryScapes",
        description="StoryScapes Theme",
        default_theme=True,
        active_theme=False,
        background_logo="theme/img/large-gov-background.png",
        primary_logo="theme/img/storyscapes-primary-logo.png",
        banner_logo="theme/img/storyscapes-banner-logo.png"
    )
    theme_storyscapes.save()


class Migration(migrations.Migration):

    dependencies = [
        ('themes', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(load_themes),
    ]
