#
# Test Creation of Thumbnails.
#


from . import ExchangeTest

from base64 import b64encode


class ThumbnailTest(ExchangeTest):

    def setUp(self):
        super(ThumbnailTest, self).setUp()

        self.login()

    def get_thumbnail(self, path):
        r = self.client.get(path)
        self.assertEqual(r.status_code, 200, "Failed to get thumbnail")
        return r

    def test_blank(self):
        r = self.client.get('/thumbnails/maps/no-id')

        # TODO: should this really return a 404
        #       *and* a blank image?
        self.assertEqual(r.status_code, 200)

        # the 'no image' gif has 713 characters in it.
        self.assertEqual(len(r.content), 713,
                         "This image does not appear to be the no image gif")

    def test_basic_upload(self, img='test_thumbnail0.png'):
        test_thumb = open(self.get_file_path(img), 'r').read()

        # post up a legend
        r = self.client.post('/thumbnails/maps/0',
                             test_thumb,
                             content_type='application/octet-stream')

        # success!
        self.assertEqual(r.status_code, 201)

    def test_overwrite(self):
        # The legend should overwrite with the new image
        # without throwing an error.

        self.test_basic_upload()

        # yes, just do it again and see if the is an error
        self.test_basic_upload(img='test_thumbnail1.png')

        # and check that we have somehting more like test_thumbnail1.png

        r = self.get_thumbnail('/thumbnails/maps/0')
        self.assertEqual(len(r.content), 4911,
                         'This does not look like thumbnail 1')

    def test_bad_image(self):

        # first a test without any thumbnail
        r = self.client.post('/thumbnails/maps/0')
        self.assertEqual(r.status_code, 400,
                         'Tried to process a missing thumbnail.')

        # now a post with a *bad* thumbnail string.
        shp_file = open(self.get_file_path('test_point.shp'), 'r')
        r = self.client.post('/thumbnails/maps/0',
                             data=shp_file,
                             content_type='application/octet-stream')
        self.assertEqual(r.status_code, 400,
                         'Tried to process a poorly formatted thumbnail.')

    def test_bad_object_type(self):
        r = self.client.post('/thumbnails/chicken/feed')
        self.assertEqual(r.status_code, 404)

    def test_huge_thumbnail(self):
        # thumbnails are limited in size, luckily we
        # can use a big random file since the size check happens
        # before the mimetype check.

        big_string = '*' * 400001

        r = self.client.post('/thumbnails/maps/0', big_string,
                             content_type='text/plain')

        self.assertEqual(r.status_code, 400)

    # The client needs to be able to upload the image as a
    # base 64 encoded string.  This tests that capability.
    #
    def test_base64_pngs(self):
        thumbpng = open(
            self.get_file_path('test_thumbnail0.png'), 'rb').read()

        header = 'data:image/png;base64,'

        base64_png = header + b64encode(thumbpng)

        r = self.client.post('/thumbnails/maps/0',
                             base64_png,
                             content_type='image/png')

        self.assertEqual(r.status_code, 201, 'Error: ' + r.content)

        # then test the correct image came back.
        r = self.client.get('/thumbnails/maps/0')
        test_b64 = b64encode(r.content)
        self.assertEqual(test_b64, b64encode(thumbpng),
                         'Images appear to differ.')

    # Ensure that layer legends are preserved when set.
    #
    def test_two_layers(self):
        png1 = open(self.get_file_path('test_thumbnail0.png'), 'rb').read()
        png2 = open(self.get_file_path('test_thumbnail1.png'), 'rb').read()

        self.client.post('/thumbnails/layers/layer1', png1,
                         content_type='image/png')

        self.client.post('/thumbnails/layers/layer2', png2,
                         content_type='image/png')

        r = self.client.get('/thumbnails/layers/layer1')
        self.assertEqual(r.status_code, 200, 'failed to retrieve thumbnail')
        data1 = r.content

        r = self.client.get('/thumbnails/layers/layer2')
        self.assertEqual(r.status_code, 200, 'failed to retrieve thumbnail')
        data2 = r.content

        self.assertEqual(data1, png1, 'Mismatch in thumbnail 1')
        self.assertEqual(data2, png2, 'Mismatch in thumbnail 2')
