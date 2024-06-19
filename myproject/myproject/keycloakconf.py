from typing import Optional

from django.conf import settings
from django.contrib.sites import requests


class KeycloakConfidentialBackend:

    @staticmethod
    def exchange_code_for_token(code: str) -> Optional[dict]:
        token_endpoint = f"{settings.KEYCLOAK_URL_BASE}realms/{settings.REALM_NAME}/protocol/openid-connect/token"
        payload = {
            'code': code,
            'grant_type': 'authorization_code',
            'client_id': settings.CLIENT_ID,
            'client_secret': settings.CLIENT_SECRET,
            'redirect_uri': '/',
        }
        response = requests.post(token_endpoint, data=payload)
        if response.status_code == 200:
            return response.json()
        return None
