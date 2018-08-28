#
# Tests that celery is running and tests
# Exchange Celery tasks.
#

from unittest import TestCase

from celery import Celery


class TestCelery(TestCase):

    def test_celery(self):
        # get a Celery "connection"
        celery = Celery()

        # This is a test task that returns the number
        # passed into the function.
        @celery.task
        def mirror(x):
            return x

        # some number.
        test_n = 44
        # kick off the celery task
        r = mirror.apply(args=(test_n,)).get()
        # ensure the number comes back.
        self.assertEqual(r, test_n)
