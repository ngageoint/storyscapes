"""
GeoAxis OAuth2 backend:
"""
import base64

from social_core.backends.oauth import BaseOAuth2

from django.conf import settings


class GeoAxisOAuth2(BaseOAuth2):
    name = 'geoaxis'
    HOST = getattr(settings, 'SOCIAL_AUTH_GEOAXIS_HOST', 'localhost')
    CLIENT_KEY = getattr(settings, 'SOCIAL_AUTH_GEOAXIS_KEY', '')
    CLIENT_SECRET = getattr(settings, 'SOCIAL_AUTH_GEOAXIS_SECRET', '')
    ID_KEY = 'user_id'
    AUTHORIZATION_URL = 'https://{0}/ms_oauth/oauth2/endpoints/' \
                        'oauthservice/authorize'.format(HOST)
    ACCESS_TOKEN_URL = 'https://{0}/ms_oauth/oauth2/endpoints/' \
                       'oauthservice/tokens'.format(HOST)
    DEFAULT_SCOPE = getattr(settings, 'SOCIAL_AUTH_GEOAXIS_SCOPE', '')
    REDIRECT_STATE = False
    ACCESS_TOKEN_METHOD = 'POST'

    EXTRA_DATA = [
        ('refresh_token', 'refresh_token', True),
        ('personatypecode', 'personatypecode'),
        ('DN', 'DN'),
        ('uri', 'uri')
    ]

    def auth_headers(self):
        b64Val = base64.b64encode('{}:{}'.format(
            self.CLIENT_KEY, self.CLIENT_SECRET))
        return {
            'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8',
            'Authorization': "Basic %s" % b64Val}

    def get_user_id(self, details, response):
        return details['uid']

    def get_user_details(self, response):
        """Return user details from GeoAxis account"""
        fullname, first_name, last_name = self.get_user_names(
            '', response.get('firstname'), response.get('lastname'))
        return {'username': response.get('username').lower(),
                'email': response.get('email').lower(),
                'fullname': fullname,
                'first_name': first_name,
                'last_name': last_name,
                'uid': response.get('uid').lower()}

    def user_data(self, access_token, *args, **kwargs):
        """Grab user profile information from GeoAxis.

        Response:

        {
            "uid": "testuser",
            "mail": "testuser@gxis.org",
            "username": "testuser",
            "DN": "cn=testuser, OU=People, OU=Unit, OU=DD, O=Example, C=US",
            "email": "testuser@gxis.org",
            "ID": "testuser",
            "lastname": "testuser",
            "login": "testuser",
            "commonname": "testuser",
            "firstname": "testuser",
            "personatypecode": "AAA",
            "uri": "\/ms_oauth\/resources\/userprofile\/me\/testuser"
        }


        """
        response = self.get_json(
            'https://' + self.HOST + '/ms_oauth/resources/userprofile/me',
            params={'access_token': access_token},
            headers={'Authorization': access_token})
        return response
