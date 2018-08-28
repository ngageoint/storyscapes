# -*- coding: utf-8 -*-
from django.core.management.base import BaseCommand
from exchange.themes.models import Theme


class Command(BaseCommand):
    help = 'List available themes by name and id'

    def handle(self, *args, **options):
        themes = Theme.objects.all()
        self.stdout.write("Available Themes:")

        for theme in themes:
            self.stdout.write("- %s [%s]" % (theme.name, theme.id))
