# myapp/middleware.py
import requests
from jose import jwt, jwk
from jose.exceptions import JWTError, ExpiredSignatureError
from django.http import JsonResponse, HttpResponseRedirect
from django.urls import reverse


class KeycloakTokenMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        jwks_url = 'http://0.0.0.0:8080/realms/my_blog/protocol/openid-connect/certs'

        try:
            jwks_response = requests.get(jwks_url)
            jwks_response.raise_for_status()
            jwks = jwks_response.json()

            authorization_header = request.META.get('HTTP_AUTHORIZATION', '')
            print(f"Authorization header value: {authorization_header}")

            if not authorization_header.startswith('Bearer '):
                raise ValueError("Invalid Authorization header. Expected format 'Bearer <token>'.")

            jwt_token = authorization_header.split('Bearer ')[1].strip()
            print(f"Extracted token: {jwt_token}")

            headers = jwt.get_unverified_headers(jwt_token)
            kid = headers.get('kid')
            if not kid:
                raise ValueError("kid not found in token headers.")

            public_key = None
            for key in jwks['keys']:
                if key['kid'] == kid:
                    public_key = jwk.construct(key)
                    break

            if not public_key:
                raise ValueError("Public key not found in JWKS")

            payload = jwt.decode(jwt_token, public_key, algorithms=['RS256'])
            request.jwt_payload = payload

        except requests.exceptions.RequestException as e:
            print(f"Error fetching JWKS: {e}")
            return JsonResponse({'error': 'Error fetching JWKS'}, status=500)

        except (KeyError, ValueError, JWTError, ExpiredSignatureError) as e:
            print(f"JWT decoding or key handling error: {e}")
            return JsonResponse({'error': str(e)}, status=401)

        response = self.get_response(request)
        return response
