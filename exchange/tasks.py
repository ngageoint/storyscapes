from celery.task import task
from celery.utils.log import get_task_logger
from geonode.catalogue import get_catalogue
from xml.sax.saxutils import escape
from geonode.services.models import Service
import datetime

logger = get_task_logger(__name__)


class UpstreamServiceImpairment(Exception):
    pass


class Record(dict):
    """dot.notation access to dictionary attributes"""
    __getattr__ = dict.get
    __setattr__ = dict.__setitem__
    __delattr__ = dict.__delitem__


@task(
    bind=True,
    max_retries=1,
)
def create_record(self, id):

    def build_service_url(service, type):
        url = service.base_url
        if type == 'WMSServer':
            url = url.replace('rest/services', 'services')
            url += 'WMSServer?request=GetCapabilities&amp;service=WMS'
        elif type == 'KmlServer':
            url += 'generateKml'
        elif type == 'FeatureServer':
            url = url.replace('MapServer', 'FeatureServer')
        elif type == 'WFSServer':
            url = url.replace('rest/services', 'services')
            url += 'WFSServer?request=GetCapabilities&amp;service=WFS'

        return {'scheme': get_types(type.lower()), 'url': url}

    def get_refs(service):
        values = []
        references = service.service_refs.split(',')
        for reference in references:
            values.append(build_service_url(service, reference.strip()))

        return values

    def get_types(server_type):

        if 'REST' in server_type or 'mapserver' in server_type:
            layer_type = 'ESRI:ArcGIS:MapServer'
        elif 'REST' in server_type or 'featureserver' in server_type:
            layer_type = 'ESRI:ArcGIS:FeatureServer'
        elif 'kml' in server_type:
            layer_type = 'OGC:KML'
        elif 'wfs' in server_type:
            layer_type = 'OGC:WFS'
        else:
            layer_type = 'OGC:WMS'

        return layer_type

    catalogue = get_catalogue()

    service = Service.objects.get(pk=id)
    service.is_published = False
    service.save()

    if service.type in ["WMS", "OWS"]:
        for record in service.servicelayer_set.all():
            item = Record({
                'uuid': record.uuid,
                'title': record.title.encode('ascii', 'xmlcharrefreplace'),
                'creator': service.owner.username,
                'record_type': get_types(service.type),
                'modified': datetime.datetime.now(),
                'typename': record.typename,
                'date': service.date,
                'abstract': record.description.encode(
                    'ascii',
                    'xmlcharrefreplace') if record.description else '',
                'format': get_types(service.type),
                'base_url': service.base_url,
                'references': [{'scheme': "OGC:WMS", 'url': service.base_url}],
                # ^^^ .join(reference_element),
                'category': escape(
                    service.category.gn_description if service.category else ''
                ),
                'contact': service.owner,
                'bbox_l': '-85.0 -180',
                # ^^^ .format(record.bbox_y1, record.bbox_x1),
                'bbox_u': '85.0 180',
                # ^^^ .format(record.bbox_y0, record.bbox_x0),
                'classification': service.classification,
                'caveat': service.caveat,
                'fees': service.fees,
                'provenance': service.provenance,
                'maintenance_frequency': service.maintenance_frequency,
                'license': service.license,
                'keywords': record.keywords,
                'title_alternate': record.typename
            })
            resp = catalogue.create_record(item)
            logger.debug(resp)
    else:
        item = Record({
            'uuid': service.uuid,
            'title': service.title.encode('ascii', 'xmlcharrefreplace'),
            'creator': service.owner.username,
            'record_type': get_types(service.type),
            'modified': datetime.datetime.now(),
            'typename': service.servicelayer_set.all()[0].typename,
            'date': service.date,
            'abstract': service.abstract.encode(
                'ascii', 'xmlcharrefreplace') if service.abstract else '',
            'format': get_types(service.type),
            'base_url': service.base_url[:-1] if service.base_url.endswith(
                '/') else service.base_url,
            'references': get_refs(service) if service.service_refs else [],
            'category': escape(
                service.category.gn_description if service.category else ''),
            'contact': 'registry',
            'bbox_l': '-85.0 -180',
            'bbox_u': '85.0 180',
            'classification': service.classification,
            'caveat': service.caveat,
            'fees': service.fees,
            'provenance': service.provenance,
            'maintenance_frequency': service.maintenance_frequency,
            'license': service.license,
            # 'keywords': service.keywords,
            'title_alternate': service.servicelayer_set.all()[0].typename
        })
        resp = catalogue.create_record(item)
        logger.debug(resp)

    service.is_published = True
    service.save()


@task(
    bind=True,
    max_retries=1,
)
def delete_record(self, id):
    """
    Remove a CSW record
    """

    catalogue = get_catalogue()
    catalogue.remove_record(id)
