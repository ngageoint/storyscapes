

from exchange import __version__ as the_version, get_version

from . import ExchangeTest


class TestGetVersion(ExchangeTest):

    def test_get_version(self):
        self.assertTrue(
            the_version in get_version(),
            '%s != %s! Bad version!' % (the_version, get_version()))
