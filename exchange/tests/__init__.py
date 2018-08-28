#
# Setup a parent class for Exchange tests
#  that handles commmon operations.
#

import django
from django.test import TestCase, Client
from django.contrib.auth import get_user_model
from django.core.management import call_command

import os.path

TESTDIR = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'files')


class ExchangeTest(TestCase):

    def setUp(self):
        django.setup()
        call_command('rebuild_index')

    def get_file_path(self, filename):
        global TESTDIR
        return os.path.join(TESTDIR, filename)

    # The test user is a basic user, no admin/staff permissions.
    #
    def create_test_user(self):
        User = get_user_model()

        test_users = User.objects.filter(
            username='test'
        )
        if test_users.count() > 0:
            self.test_user = test_users[0]
        else:
            self.test_user = User.objects.create_user(
                username='test',
                email=''
            )
        self.test_user.set_password('test')
        self.test_user.save()

        return ('test', 'test')

    # Admin user is the overlord for the system.
    #
    def create_admin_user(self):
        User = get_user_model()

        admin_users = User.objects.filter(
            is_superuser=True
        )
        if admin_users.count() > 0:
            self.admin_user = admin_users[0]
        else:
            self.admin_user = User.objects.create_superuser(
                username='admin',
                email='',
                password='admin',
            )
        self.admin_user.set_password('admin')
        self.admin_user.save()

        return ('admin', 'admin')

    def login(self, asTest=False):
        if(asTest):
            username, password = self.create_test_user()
        else:
            username, password = self.create_admin_user()

        self.client = Client()
        logged_in = self.client.login(
            username=username,
            password=password
        )
        self.assertTrue(logged_in)

        self.expected_status = 200

        return True
