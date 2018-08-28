from django.conf.urls import patterns, url, include
from api import FileItemResource

fileitem_resource = FileItemResource()

urlpatterns = patterns(
    '',
    url(r'^api/', include(fileitem_resource.urls)),
)
