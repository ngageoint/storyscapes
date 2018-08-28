from __future__ import unicode_literals
from django.db import migrations


def load_themes(apps, schema_editor):
    Theme = apps.get_model("themes", "Theme")
    theme_geoint = Theme(
        name="GEOINT",
        description="GEOINT Services Theme",
        default_theme=True,
        active_theme=False,
        title=" ",
        background_logo="theme/img/geoint-background.png",
        primary_logo="theme/img/geoint-primary-logo.png",
        banner_logo="theme/img/geoint-banner-logo.png"
    )
    theme_geoint.save()
    theme_commercial = Theme(
        name="Commercial",
        description="Commercial Theme",
        default_theme=True,
        active_theme=False,
        background_logo="theme/img/commercial-background.png"
    )
    theme_commercial.save()
    theme_largegov = Theme(
        name="Large Government",
        description="Large Government Theme",
        default_theme=True,
        active_theme=False,
        background_logo="theme/img/large-gov-background.png"
    )
    theme_largegov.save()
    theme_smallgov = Theme(
        name="Small Government",
        description="Small Government Theme",
        default_theme=True,
        active_theme=False,
        background_logo="theme/img/small-gov-background.png"
    )
    theme_smallgov.save()


class Migration(migrations.Migration):

    dependencies = [
        ('themes', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(load_themes),
    ]
