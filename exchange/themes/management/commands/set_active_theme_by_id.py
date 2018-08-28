# -*- coding: utf-8 -*-
from django.core.management.base import BaseCommand, CommandError
from exchange.themes.models import Theme
from optparse import make_option


class Command(BaseCommand):
    help = 'Set a specific Theme by id as the active Theme.'
    option_list = BaseCommand.option_list + (
        make_option(
            '--t',
            '--theme_id',
            action='store',
            dest='theme_id',
            type='int'),
    )

    def handle(self, *args, **options):
        theme_id = options['theme_id']
        if not theme_id:
            self.stdout.write('\nYou need to pass the --theme_id argument\n')
        else:
            try:
                theme = Theme.objects.get(id=theme_id)
            except Theme.DoesNotExist:
                raise CommandError('Theme id "%s" does not exist' % theme_id)

            theme.active_theme = True
            theme.save()

            self.stdout.write('Successfully activated theme "%s"' % theme.name)
