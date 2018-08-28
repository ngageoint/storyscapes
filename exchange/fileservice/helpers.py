from django.conf import settings
import os


def get_streaming_supported():
    """
    example settings file
    FILESERVICE_CONFIG = {
        'streaming_supported': True
    }
    """
    conf = getattr(settings, 'FILESERVICE_CONFIG', {})
    return conf.get('streaming_supported', False)


def get_fileservice_dir():
    """
    example settings file
    FILESERVICE_CONFIG = {
        'store_dir': '/var/lib/geoserver_data/fileservice_store'
    }
    """
    conf = getattr(settings, 'FILESERVICE_CONFIG', {})
    dir = conf.get(
        'store_dir', os.path.join(settings.MEDIA_ROOT, 'fileservice'))
    return os.path.normpath(dir) + os.sep


def get_fileservice_whitelist():
    conf = getattr(settings, 'FILESERVICE_CONFIG', {})
    return [x.lower() for x in conf.get('types_allowed', [])]


def u_to_str(string):
    return string.encode('ascii', 'ignore')


def get_fileservice_files():
    return os.listdir(get_fileservice_dir())


def get_filename_absolute(filename):
    return '{}/{}'.format(get_fileservice_dir(), filename)
