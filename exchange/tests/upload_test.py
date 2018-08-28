# Perform tests against the uploader.
#
#


import re

from . import ExchangeTest
from exchange.tests.osgeo_importer_upload_test import UploaderMixin

import pytest


# This is a dummy exception class
#  used to make back tracing easier.
class UploaderException(Exception):
    pass


# Sift through the HTML for the Javascript defined
#  bounding box.
def parse_bbox_from_html(html):
    p = re.compile('"bbox": ' +
                   '\[([0-9\-\.]+), ([0-9\-\.]+), ' +
                   '([0-9\-\.]+), ([0-9\-\.]+)\]')

    bboxes = p.findall(html)

    if(len(bboxes) > 0):
        return [float(x) for x in bboxes[0]]
    return None


class TestBBOXParser(ExchangeTest):

    def test_invalid_bbox(self):
        self.assertIsNone(parse_bbox_from_html(''),
                          'BBOX parser failed to fail properly')


# Test class for uploading layer
#
# Performs various uploads and drops of layers.
#

class UploadLayerTest(UploaderMixin, ExchangeTest):

    def setUp(self):
        super(UploadLayerTest, self).setUp()
        self.login()

    # This is a meta function for executing uploader options.
    #
    # Uploads the shapefile, checks on the layer, and drops it.
    #
    def _test_meta(self, shapefile, uploaderParams={}):
        self.upload_shapefile(shapefile, uploaderParams)
        self.drop_layers()

    # Test an upload to geogig of a basic single-point shapefile.
    @pytest.mark.skip(
        reason="Geogig not quite working with configured Geoserver")
    def test_geogig_upload(self):
        data_path = './test_point.'

        shapefile = {
            'base_file': data_path + 'shp',
            'dbf_file': data_path + 'dbf',
            'shx_file': data_path + 'shx',
            'prj_file': data_path + 'prj'
        }

        params = {
            'geoserver_store': {'type': 'geogig'},
            'geogig_store': 'NoseTests'
        }

        self._test_meta(shapefile, uploaderParams=params)

    # Test uploading a basic geojson file.
    # 20 March 2017: Test being skipped as not all uploaders
    #                support GeoJson
    def _test_geojson_upload(self):
        shapefile = {
            'base_file': './bbox.geojson'
        }
        self._test_meta(shapefile)

    # Test the BBOX of a layer when it's been uploaded to GeoGig
    #  against when it has not been uploaded to GeoGig.
    #
    # Refs: NODE-804
    @pytest.mark.skip(
        reason="Geogig not quite working with configured Geoserver")
    def test_bbox_issues(self):
        data_path = './test_point.'

        shapefile = {
            'base_file': data_path + 'shp',
            'dbf_file': data_path + 'dbf',
            'shx_file': data_path + 'shx',
            'prj_file': data_path + 'prj'
        }

        params = {
            'geoserver_store': {'type': 'geogig'},
            'geogig_store': 'NoseTests'
        }

        geogig_layer = self.upload_shapefile(shapefile, uploaderParams=params)
        geogig_layer_uri = self.layer_uri(geogig_layer)

        # ensure the url exists
        self.assertIsNotNone(geogig_layer_uri,
                             "Bad URI for geogig layer")

        # get the layer data
        geogig_layer_info = self.client.get(geogig_layer_uri)

        # ensure "GeoGig" exists in the layer
        self.assertIn('GeoGig', geogig_layer_info.content)

        # pull the BBOX out of the Geogig layer
        geogig_bbox = parse_bbox_from_html(geogig_layer_info.content)

        self.assertIsNotNone(geogig_bbox,
                             "No bounding box found in Geogig Layer!")

        # second time around, no GeoGig
        params = {
        }

        layer = self.upload_shapefile(shapefile, params)
        layer_uri = self.layer_uri(layer)
        self.assertIsNotNone(layer_uri, "Failed to get valid layer_uri!")
        layer_info = self.client.get(layer_uri)
        self.assertNotIn('GeoGig', layer_info.content)

        bbox = parse_bbox_from_html(layer_info.content)

        self.assertIsNotNone(bbox,
                             "No bounding box found in non-Geogig Layer!")

        # convert the bounding boxes to strings
        #  for reporting
        s_geogig_bbox = ','.join(str(x) for x in geogig_bbox)
        s_bbox = ','.join(str(x) for x in bbox)

        # the bounding boxes are reprojected from 4326 to 3857,
        #  if the bboxes are within a metre of each other then that's a
        #  close enough match to satisfy the test.
        for i in range(4):
            t = geogig_bbox[i] - bbox[i]
            self.assertTrue(-1 <= t and t <= 1,
                            "Mismatched bounding Boxes! %s (geogig) != %s" % (
                                s_geogig_bbox, s_bbox
                            ))


class NonAdminUploadTest(UploaderMixin, ExchangeTest):

    def setUp(self):
        super(NonAdminUploadTest, self).setUp()
        # test user is not an admin
        self.login(asTest=True)

    # This is a meta function for executing uploader options.
    #
    # Uploads the shapefile, checks on the layer, and drops it.
    #
    def _test_meta(self, shapefile, uploaderParams={}):
        self.upload_shapefile(shapefile, uploaderParams)
        self.drop_layers()

    # Test an upload to geogig of a basic single-point shapefile.
    #
    @pytest.mark.skip(
        reason="Geogig not quite working with configured Geoserver")
    def test_geogig_upload(self):
        data_path = './test_point.'
        shapefile = [data_path + x for x in ['prj', 'shp', 'shx', 'dbf']]

        shapefile = {
            'base_file': data_path + 'shp',
            'dbf_file': data_path + 'dbf',
            'shx_file': data_path + 'shx',
            'prj_file': data_path + 'prj'
        }

        params = {
            'geoserver_store': {'type': 'geogig'},
            'geogig_store': 'NoseTests'
        }

        self._test_meta(shapefile, uploaderParams=params)
