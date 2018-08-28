
from django.conf.urls import url

from .views import thumbnail_view
from .tasks import register_post_save_functions

urlpatterns = (
    url(r'^thumbnails/(?P<objectType>maps|documents|layers)/(?P<objectId>.+)$',
        thumbnail_view, name='thumbnail_handler'),
)

register_post_save_functions()
