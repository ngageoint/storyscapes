from tastypie.test import ResourceTestCaseMixin
from django.core.files.uploadedfile import SimpleUploadedFile
from exchange import settings
from exchange.fileservice.api import FileItemResource
from django.http import HttpResponse
from mock import mock_open
import mock

from . import ExchangeTest


class FileItemResourceTest(ResourceTestCaseMixin, ExchangeTest):

    def setUp(self):
        super(FileItemResourceTest, self).setUp()

        # turn on streaming_support so that test_view can test the
        # view endpoint
        # without streaming_supported set to True, view endpoint
        # will behave exactly like download
        settings.FILESERVICE_CONFIG['streaming_supported'] = True

        self.image_filename = 'image.jpg'

        self.image_file = SimpleUploadedFile(
            name=self.image_filename,
            content='',
            content_type='image/jpg',
        )

        self.upload_url = '/api/fileservice/'
        self.download_url_template = '/api/fileservice/download/{0}'
        self.view_url_template = '/api/fileservice/view/{0}'

    @mock.patch('exchange.fileservice.api.open', mock_open())
    def test_upload(self):
        self.login()
        resp = self.client.post(
            self.upload_url, {'file': self.image_file}, follow=True)
        self.assertHttpCreated(resp)

    @mock.patch('exchange.fileservice.api.serve')
    @mock.patch('exchange.fileservice.api.os.path.isfile')
    def test_download(self, isfile_mock, serve_mock):
        isfile_mock.return_value = True
        serve_mock.return_value = HttpResponse('Empty Response')
        self.login()
        resp = self.client.get(
            self.download_url_template.format(
                self.image_filename), follow=True)
        self.assertEquals(
            resp.get('Content-Disposition'),
            'attachment; filename="{}"'.format(self.image_filename))

    @mock.patch('exchange.fileservice.api.os.path.isfile')
    def test_download_not_found(self, isfile_mock):
        isfile_mock.return_value = False
        self.login()
        resp = self.client.get(
            self.download_url_template.format(
                self.image_filename), follow=True)
        self.assertHttpNotFound(resp)

    def test_view(self):
        self.login()
        resp = self.client.get(
            self.view_url_template.format(
                self.image_filename), follow=True)
        '''
        the view end point is meant for playing back video with random access
         which means the progress indicator can be dragged around. FO the
         random access to work properly, instead of django serving up the
         video, nginx or apache have to serve it up and the fileservice adds
         the 'X-Sendfile' and the equivalent 'X-Accel-Redirect' so that
        they take it from there. Even if that happens, at least one of the
        headers should technically be present.
        '''
        self.assertTrue(
            resp.get('X-Sendfile') or resp.get('X-Accel-Redirect'))

    def test_upload_whitelist(self):
        settings.FILESERVICE_CONFIG['types_allowed'] = ['.txt']
        self.login()
        resp = self.client.post(
            self.upload_url, {'file': self.image_file}, follow=True)
        self.assertHttpBadRequest(resp)

    @mock.patch('exchange.fileservice.helpers.get_fileservice_files')
    def test_statics(self, get_fileservice_files_mock):
        get_fileservice_files_mock.return_value = ['a.jpg', 'b.jpg']
        item = FileItemResource.get_file_item_by_name('a.jpg')
        self.assertTrue(item.name == 'a.jpg')
