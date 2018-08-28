# -*- coding: utf-8 -*-
from django.core.management.base import BaseCommand, CommandError
from exchange.themes.models import Theme
from optparse import make_option


class Command(BaseCommand):
    help = 'Set a specific Theme by name as the active Theme.'
    option_list = BaseCommand.option_list + (
        make_option(
            '--t',
            '--theme_name',
            action='store',
            dest='theme_name',
            type='string'),
    )

    def handle(self, *args, **options):
        theme_name = options['theme_name']
        if not theme_name:
            self.stdout.write('\nYou need to pass the --theme_name argument\n')
        else:
            try:
                theme = Theme.objects.get(name=theme_name)
            except Theme.DoesNotExist:
                raise CommandError(
                    'Theme name "%s" does not exist' % theme_name)

            theme.active_theme = True
            theme.save()

            self.stdout.write('Successfully activated theme "%s"' % theme.name)
