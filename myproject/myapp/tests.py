from django.test import TestCase
import jwt


# Полезная нагрузка (payload), которую мы хотим включить в токен
payload = {'username': 'example_user', 'role': 'admin'}

# Секретный ключ для подписи токена
secret_key = 'zlaT0yLM2o9sULphH1c1vBnlEMTaDTpO'

# Создание JWT токена с использованием алгоритма подписи RS256
encoded_jwt = jwt.encode(payload, secret_key, algorithm='HS256')

print(encoded_jwt)


import jwt

# Ваш JWT токен
encoded_jwt = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6ImV4YW1wbGVfdXNlciIsInJvbGUiOiJhZG1pbiJ9._wZFXmkXcAH30OxuDM0dq-ETShvfwIdK4ZE7rs-fdf8'

# Секретный ключ, который использовался для создания токена
secret_key = 'zlaT0yLM2o9sULphH1c1vBnlEMTaDTpO'

try:
    # Проверка и декодирование токена
    decoded_token = jwt.decode(encoded_jwt, secret_key, algorithms=['HS256'])
    print('Декодированный токен:')
    print(decoded_token)
except jwt.ExpiredSignatureError:
    print('Ошибка: Время жизни токена истекло')
except jwt.InvalidTokenError:
    print('Ошибка: Неверный токен или подпись')
