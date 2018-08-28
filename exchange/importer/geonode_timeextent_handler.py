import logging
from django import db
from django.conf import settings
from osgeo_importer.handlers import ImportHandlerMixin
from osgeo_importer.handlers import ensure_can_run
from osgeo_importer.utils import quote_ident
from geonode.layers.models import Layer
from osgeo_importer.handlers.geonode.backward_compatibility import set_attributes  # noqa
from django.contrib.auth import get_user_model

User = get_user_model()
logger = logging.getLogger(__name__)
logger.setLevel('DEBUG')


class GeoNodeTimeExtentHandler(ImportHandlerMixin):
    """
    Sets time extent from data in postgis
    """

    def can_run(self, layer, layer_config, *args, **kwargs):
        """
        Check that geonode layer already exists
        Check that start or end time column exists
        """
        if layer_config['raster']:
            return False

        self.has_start = 'start_date' \
                         in layer_config \
                         and layer_config['start_date'] is not None
        self.has_end = 'end_date' \
                       in layer_config \
                       and layer_config['end_date'] is not None
        logger.debug(
            'Can run for Configuring time extent for %s. '
            'has_start=%s, has_end=%s',
            layer, self.has_start, self.has_end)
        self.geonode_layer = Layer.objects.get(name=layer)

        return (self.geonode_layer and (self.has_start or self.has_end))

    @ensure_can_run
    def handle(self, layer, layer_config, *args, **kwargs):
        """
        Gets existing geonode layer and configures time extents
        by querying postgresql data table
        """

        # Configure time extent

        if self.has_start:
            logger.debug(
                'Configuring Start Date Range for column %s',
                layer_config['start_date'])
            start_date_col = quote_ident(layer_config['start_date'])

        if self.has_end:
            logger.debug(
                'Configuring End Date Range for column %s',
                layer_config['end_date'])
            end_date_col = quote_ident(layer_config['end_date'])

        conn = db.connections[settings.OSGEO_DATASTORE]
        cursor = conn.cursor()
        scrub_layer_name = quote_ident(layer)
        logger.debug('Getting min/max for %s', scrub_layer_name)

        mint = None
        maxt = None

        if self.has_start and self.has_end:
            query = 'SELECT min(%s), max(%s) FROM %s;' % (
                start_date_col, end_date_col, scrub_layer_name)
        elif self.has_start:
            query = 'SELECT min(%s), max(%s) FROM %s;' % (
                start_date_col, start_date_col, scrub_layer_name)
        elif self.has_end:
            query = 'SELECT min(%s), max(%s) FROM %s;' % (
                end_date_col, end_date_col, scrub_layer_name)
        cursor.execute(query)
        mint, maxt = cursor.fetchone()

        logger.debug('mint %s maxt %s', mint, maxt)

        self.geonode_layer.temporal_extent_start = mint
        self.geonode_layer.temporal_extent_end = maxt
        self.geonode_layer.save()

        return 'Temporal Extent Configured'
