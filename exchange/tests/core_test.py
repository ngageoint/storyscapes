from django.test import TestCase
from exchange.core.context_processors import resource_variables
from urlparse import urlparse


class MockRequest:
    pass


request = MockRequest()


class resource_variablesTestCase(TestCase):

    def setUp(self):
        self.defaults = resource_variables(request)

    def test(self):
        self.assertIn(
            'VERSION',
            self.defaults
        )
        self.assertIn(
            'MAP_CRS',
            self.defaults
        )
        self.assertIn(
            'INSTALLED_APPS',
            self.defaults
        )
        self.assertIn(
            'GEOAXIS_ENABLED',
            self.defaults
        )
        self.assertIn(
            'NOMINATIM_ENABLED',
            self.defaults
        )
        self.assertIn(
            'GEOQUERY_ENABLED',
            self.defaults
        )
        self.assertIn(
            'NOMINATIM_URL',
            self.defaults
        )
        self.assertIn(
            'GEOQUERY_URL',
            self.defaults
        )

        if self.defaults['GEOQUERY_ENABLED'] is True:
            self.assertIsNotNone(self.defaults['GEOQUERY_URL'],
                                 "GEOQUERY_URL was not defined.")
            # Minimal validation that GEOQUERY_URL is a valid URL
            self.assertNotEqual(
                urlparse(self.defaults['GEOQUERY_URL']).netloc, '')
