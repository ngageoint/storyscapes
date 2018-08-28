# Perform tests for auditing.
from . import ExchangeTest
from exchange.audit.models import AuditEvent


class AuditTest(ExchangeTest):

    def test(self):
        self.login()
        last_event = AuditEvent.objects.latest('datetime')
        self.assertEquals(last_event.event, 'login')
        self.client.logout()
        last_event = AuditEvent.objects.latest('datetime')
        self.assertEquals(last_event.event, 'logout')
        self.client.login(
            username='bogus',
            password='bogus'
        )
        last_event = AuditEvent.objects.latest('datetime')
        self.assertEquals(last_event.event, 'failed_login')


class AuditAdminTest(ExchangeTest):

    def setUp(self):
        super(AuditAdminTest, self).setUp()

        self.login()

    def test_model_admin(self):
        r = self.client.get('/admin/audit/auditevent/')

        self.assertEqual(
            r.status_code, 200,
            'Did not get admin audit event list (status: %d)' % (
                r.status_code))
