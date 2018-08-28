from django.test import TestCase
from mock import Mock
from exchange.auth.middleware import GeoAxisMiddleware
from exchange.auth.backends.geoaxis import GeoAxisOAuth2
from exchange.auth.backends.auth0 import AuthZeroOAuth2


class GeoAxisMiddlewareTest(TestCase):

    def setUp(self):
        self.geo_axis = GeoAxisMiddleware()
        self.request = Mock()
        self.request.session = {}
        self.request.META = {}  # { 'OAM_REMOTE_USER': 'test_user'}

    def test_header_name(self):
        self.assertEqual(self.geo_axis.header, 'OAM_REMOTE_USER')


class AuthZeroOAuth2Test(TestCase):

    def setUp(self):
        self.geo_axis = AuthZeroOAuth2(Mock())
        self.request = Mock()
        self.HOST = 'example.com'
        self.admin_roles = 'admin'
        self.allowed_roles = 'admin'

    def test_get_user_details_admin(self):
        response = {
            "nickname": "testuser",
            "mail": "testuser@gxis.org",
            "username": "testuser",
            "organization": "cn=testuser, OU=People, OU=Unit,"
                            "OU=DD, O=Example, C=US",
            "email": "testuser@gxis.org",
            "ID": "testuser",
            "lastname": "testuser",
            "uid": "testuser",
            "commonname": "testuser",
            "firstname": "testuser",
            "user_metadata": {"name": "testuser",
                              "firstName": "testuser",
                              "lastName": "testuser", },
            "app_metadata": {"SiteRole": 'admin'}
        }
        self.assertTrue(
            'is_active' in self.geo_axis.get_user_details(response))

    def test_get_user_details_non_admin(self):
        response = {
            "nickname": "testuser",
            "mail": "testuser@gxis.org",
            "username": "testuser",
            "organization": "cn=testuser, OU=People, OU=Unit,"
                            "OU=DD, O=Example, C=US",
            "email": "testuser@gxis.org",
            "ID": "testuser",
            "lastname": "testuser",
            "uid": "testuser",
            "commonname": "testuser",
            "firstname": "testuser",
            "user_metadata": {"name": "testuser",
                              "firstName": "testuser",
                              "lastName": "testuser", },
            "app_metadata": {"SiteRole": 'non_admin'}
        }
        self.allowed_roles = ['']
        self.assertTrue(
            'is_active' in self.geo_axis.get_user_details(response))


class GeoAxisOAuth2Test(TestCase):

    def setUp(self):
        self.geo_axis = GeoAxisOAuth2(Mock())
        self.request = Mock()
        self.request.session = {}
        self.request.META = {}  # { 'OAM_REMOTE_USER': 'test_user'}
        self.HOST = 'example.com'

    def test_auth_headers(self):
        self.assertTrue('Authorization' in self.geo_axis.auth_headers())

    def test_user_id(self):
        self.assertEqual(
            '1234', self.geo_axis.get_user_id({'uid': '1234'}, {}))

    def test_get_user_details(self):
        response = {
            "uid": "testuser",
            "mail": "testuser@gxis.org",
            "username": "testuser",
            "DN": "cn=testuser, OU=People, OU=Unit, OU=DD,"
                  "O=Example, C=US",
            "email": "testuser@gxis.org",
            "ID": "testuser",
            "lastname": "testuser",
            "login": "testuser",
            "commonname": "testuser",
            "firstname": "testuser",
            "personatypecode": "AAA",
            "uri": "\/ms_oauth\/resources\/userprofile\/me\/testuser"
        }
        self.assertTrue(
            'username' in self.geo_axis.get_user_details(response))
