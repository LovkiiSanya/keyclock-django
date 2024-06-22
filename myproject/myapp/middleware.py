import requests
from jose import jwt, jwk
from django.http import JsonResponse


class KeycloakTokenMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        jwks_url = 'http://0.0.0.0:8080/realms/my_blog/protocol/openid-connect/certs'

        try:
            # Получаем JWKS с Keycloak
            jwks_response = requests.get(jwks_url)
            jwks_response.raise_for_status()
            jwks = jwks_response.json()

            # Получаем JWT из заголовка Authorization
            authorization_header = request.META.get('HTTP_AUTHORIZATION', '')

            if not authorization_header.startswith('Bearer '):
                raise ValueError("Invalid Authorization header. Expected format 'Bearer <token>'.")

            jwt_token = authorization_header.split('Bearer ')[1].strip()

            # Извлекаем kid из заголовков JWT
            headers = jwt.get_unverified_headers(jwt_token)
            kid = headers.get('kid')

            if not kid:
                raise ValueError("kid not found in token headers.")

            public_key = None

            # Находим открытый ключ по kid в JWKS
            for key in jwks['keys']:
                if key['kid'] == kid:
                    public_key = jwk.construct(key)
                    break

            if not public_key:
                raise ValueError("Public key not found in JWKS")

            # Проверяем и декодируем JWT
            payload = jwt.decode(jwt_token, public_key, algorithms=['RS256'])
            request.jwt_payload = payload

        except requests.exceptions.RequestException as e:
            # Обработка ошибок сети или запроса к JWKS
            print(f"Error fetching JWKS: {e}")
            return JsonResponse({'error': 'Error fetching JWKS'}, status=500)

        except (KeyError, ValueError) as e:
            # Обработка ошибок декодирования JWT или работы с ключами
            print(f"JWT decoding or key handling error: {e}")
            return JsonResponse({'error': str(e)}, status=401)

        # Продолжаем выполнение запроса
        response = self.get_response(request)
        return response
