import requests
from django.http import HttpResponse
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from .models import Blog, Comment
from .serrializer import BlogSerializer, CommentSerializer
from django.shortcuts import render
from django.shortcuts import redirect
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Blog, Comment


class BlogViewSet(viewsets.ModelViewSet):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


def home(request):
    return HttpResponse("Home Page")


def login_page(request):
    return render(request, 'myapp/login.html')


def keycloak_login(request):
    keycloak_url = 'http://0.0.0.0:8080/realms/my_blog/protocol/openid-connect/auth'
    client_id = 'my_blog'
    redirect_uri = 'http://127.0.0.1:8000/myapp/keycloak_callback/'
    state = 'some_random_state'
    login_url = f"{keycloak_url}?client_id={client_id}&redirect_uri={redirect_uri}&state={state}&response_type=code"
    return redirect(login_url)


def keycloak_callback(request):
    code = request.GET.get('code')
    state = request.GET.get('state')
    error = request.GET.get('error')

    if error:
        return HttpResponse(f"Keycloak error: {error}")

    if not code or not state:
        return HttpResponse("Missing code or state parameter", status=400)

    token_url = 'http://0.0.0.0:8080/realms/my_blog/protocol/openid-connect/token'
    client_id = 'my_blog'
    client_secret = 'zlaT0yLM2o9sULphH1c1vBnlEMTaDTpO'
    redirect_uri = 'http://127.0.0.1:8000/myapp/keycloak_callback/'

    data = {
        'grant_type': 'authorization_code',
        'code': code,
        'redirect_uri': redirect_uri,
        'client_id': client_id,
        'client_secret': client_secret
    }

    headers = {
        'Content-Type': 'application/x-www-form-urlencoded'
    }

    response = requests.post(token_url, data=data, headers=headers)

    try:
        response_data = response.json()
    except ValueError as e:
        return HttpResponse(f"Error decoding JSON response: {str(e)}. Response content: {response.content}", status=500)

    if 'access_token' in response_data:
        access_token = response_data['access_token']
        request.session['access_token'] = access_token
        request.session['refresh_token'] = response_data.get('refresh_token')
        return HttpResponse(f"Access token: {access_token}")
    else:
        return HttpResponse(f"Error: {response_data}", status=500)


def logout(request):
    request.session.flush()
    return redirect('home')
