#
# API for handling Thumbnails in Exchange.
#

from django.db import models


class Thumbnail(models.Model):
    object_type = models.CharField(max_length=255,
                                   blank=False)
    object_id = models.CharField(max_length=255, blank=False)

    thumbnail_mime = models.CharField(max_length=127, null=True, blank=True)
    thumbnail_img = models.BinaryField(null=True, blank=True)

    is_automatic = models.BooleanField(default=False)

    class Meta:
        unique_together = ('object_type', 'object_id')


# This function properly handles updating vs inserting
# for a thumbnail. Django ".save" was not properly dealing
# with the composite primary key.
#
def save_thumbnail(objectType, objectId, mime, img, automatic=False):
    thumb = None
    try:
        thumb = Thumbnail.objects.get(
            object_type=objectType, object_id=objectId)
    except Thumbnail.DoesNotExist:
        thumb = Thumbnail(object_type=objectType, object_id=objectId)

    # set the image and the mime type
    thumb.thumbnail_mime = mime
    thumb.thumbnail_img = img
    thumb.is_automatic = automatic

    # save the thumbnail
    thumb.save()


# Check to see if this is an 'automatic' type
# of thumbnail.
#
# If "is_automatic" is set to true then Exchange/GeoServer
# will generate the thumbnail for the layer.  When it is set to False,
# that means the user has set a thumbnail and it will not be updated
# when the signals trigger it.
#
def is_automatic(objectType, objectId):
    try:
        t = Thumbnail.objects.get(
            object_type=objectType, object_id=objectId)
    # when no legend exists, then one should be generated automatically.
    except Thumbnail.DoesNotExist:
        return True

    return t.is_automatic
