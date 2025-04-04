import json

import gspread
from google.oauth2 import service_account

from config import GOOGLE_CLIENT_ID, GOOGLE_PROJECT_ID, GOOGLE_AUTH_URI, GOOGLE_TOKEN_URI, \
    GOOGLE_AUTH_PROVIDER_X509_CERT_URL, GOOGLE_CLIENT_SECRET, GOOGLE_CLIENT_EMAIL, GOOGLE_TYPE, GOOGLE_PRIVATE_KEY_ID, \
    GOOGLE_PRIVATE_KEY, GOOGLE_CLIENT_X509_CERT_URL, GOOGLE_UNIVERSE_DOMAIN

service_account_info = {
    "client_id": GOOGLE_CLIENT_ID,
    "project_id": GOOGLE_PROJECT_ID,
    "auth_uri": GOOGLE_AUTH_URI,
    "token_uri": GOOGLE_TOKEN_URI,
    "auth_provider_x509_cert_url": GOOGLE_AUTH_PROVIDER_X509_CERT_URL,
    "client_secret": GOOGLE_CLIENT_SECRET,
    "client_email": GOOGLE_CLIENT_EMAIL,
    "type": GOOGLE_TYPE,
    "private_key_id": GOOGLE_PRIVATE_KEY_ID,
    "private_key": GOOGLE_PRIVATE_KEY.replace('\\n', '\n'),
    "client_x509_cert_url": GOOGLE_CLIENT_X509_CERT_URL,
    "universe_domain": GOOGLE_UNIVERSE_DOMAIN
}

scopes = [
    'https://www.googleapis.com/auth/spreadsheets.readonly',
    'https://www.googleapis.com/auth/drive.metadata.readonly'
]

credentials = service_account.Credentials.from_service_account_info(
    service_account_info,
    scopes=scopes
)


gc = gspread.authorize(credentials)
