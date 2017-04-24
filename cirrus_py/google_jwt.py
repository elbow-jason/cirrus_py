
import calendar
import time

import jwt
import requests

from cirrus_py.credentials import ServiceAccountCredentials

TOKEN_URL = "https://www.googleapis.com/oauth2/v4/token"
EXPIRES_AFTER = 3600 # sec
GRANT_TYPE = "urn:ietf:params:oauth:grant-type:jwt-bearer"
CREDS_ERR = Exception("credentials kwarg requires a ServiceAccountCredentials instance")
SCOPE_ERR = Exception("scope kwarg is required by GoogleJwt")

def seconds_after_epoch():
    """
    seconds since epoch
    """
    return int(calendar.timegm(time.gmtime()))


class GoogleJwt(object):
    """
    kwargs:

        scope (string; required)
            examples of valid scopes for storage:
                https://cloud.google.com/storage/docs/authentication#oauth-scopes

        credentials (credentials.ServiceAccountCredentials; required)
            get service account credentials from:
                https://console.developers.google.com/iam-admin/serviceaccounts

    methods:
        get_token() - raises or returns a dict of:
            {
                'access_token': (string) the token itself,
                'expires_in':   (int)    time in seconds until the token expires,
                'token_type':   (string) literally 'Bearer',
            }
    """
    def __init__(self, scope=None, credentials=None):
        now = seconds_after_epoch()
        if scope is None:
            raise SCOPE_ERR
        if not isinstance(credentials, ServiceAccountCredentials):
            raise CREDS_ERR
        self.scope = scope
        self._private_key = credentials.private_key()
        self.iss = credentials.client_email()
        self.aud = TOKEN_URL
        self.iat = now
        self.exp = now + EXPIRES_AFTER

    def to_dict(self):
        """
        a dict
        """
        return {
            "scope": self.scope,
            "iss":   self.iss,
            "aud":   self.aud,
            "iat":   self.iat,
            "exp":   self.exp,
        }

    def get_token(self):
        """
        returns a token or raises
        """
        kwargs = dict(
            data=self._request_data(),
            headers=self._request_headers(),
        )
        resp = requests.post(TOKEN_URL, **kwargs)
        if not resp.ok:
            raise Exception("Failed to get_token() - {}".format(resp.json()))
        return resp.json()

    def _generate_jwt(self):
        return jwt.encode(self.to_dict(), self._private_key, algorithm='RS256')

    def _request_data(self):
        return {
            "grant_type": GRANT_TYPE,
            "assertion":  self._generate_jwt(),
        }

    def _request_headers(self):
        return {
            "content-type": "application/x-www-form-urlencoded",
        }
