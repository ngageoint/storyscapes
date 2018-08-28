
from osgeo_importer.handlers import ImportHandlerMixin
from osgeo_importer.handlers import ensure_can_run
from geonode.layers.models import Layer


class GeoNodePostImportHandler(ImportHandlerMixin):
    """
    Save the geonode layer after import to trigger post save actions.
    """

    def can_run(self, layer, layer_config, *args, **kwargs):
        for name in [layer, layer_config.get(
                'name', None), layer_config.get('layer_name', None)]:
            try:
                self.geonode_layer = Layer.objects.get(name=name)
                return True
            except:
                pass

        return False

    @ensure_can_run
    def handle(self, layer, layer_config, *args, **kwargs):
        self.geonode_layer.save()
        return 'Layer Saved'
