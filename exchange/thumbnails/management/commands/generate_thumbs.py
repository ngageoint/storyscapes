from django.core.management.base import BaseCommand

from geonode.maps.models import Map
from geonode.maps.models import Layer
from exchange.thumbnails.tasks import generate_thumbnail


class Command(BaseCommand):
    help = ('Generate Auto Thumbs for all Layers/Maps that are set to auto.\n')

    def handle(self, *args, **options):
        for map in Map.objects.all():
            generate_thumbnail(map, Map)
        for layer in Layer.objects.all():
            generate_thumbnail(layer, Layer)
