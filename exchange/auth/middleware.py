from django.conf import settings
from django.contrib.auth.middleware import RemoteUserMiddleware


class GeoAxisMiddleware(RemoteUserMiddleware):
    """
    Middleware for utilizing GEOAXIS provided authentication. This is a
    subclass of the RemoteUserMiddleware. The header value is configurable
    by setting a django setting of GEOAXIS_HEADER.
    """
    header = getattr(settings, 'GEOAXIS_HEADER', 'OAM_REMOTE_USER')
    force_logout_if_no_header = False
