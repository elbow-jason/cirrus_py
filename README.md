# cirrus_py

## Usage
```python
from cirrus_py.credentials import ServiceAccountCredentials
from cirrus_py.google_jwt import GoogleJwt

# Keep them secret
creds = ServiceAccountCredentials("./my_secret_service_account_credentials.json")

STORAGE_FULL_CONTROL_SCOPE = "https://www.googleapis.com/auth/devstorage.full_control"
# see https://cloud.google.com/storage/docs/authentication#oauth-scopes for more examples
# or see https://developers.google.com/identity/protocols/googlescopes for many, many examples

my_jwt = GoogleJwt(scope=STORAGE_FULL_CONTROL_SCOPE, credentials=creds)
my_jwt.get_token()
{
  'access_token': "<access_token_here>",
  'expires_in':   3600,
  'token_type':   'Bearer'
}
```

## Links

  + [Google OAuth 2.0 API scopes](https://developers.google.com/identity/protocols/googlescopes)