from django.urls import path
from django.contrib.auth import views as auth_views
from .views import home, keycloak_login, keycloak_callback

urlpatterns = [
    path('', home, name='home_page'),
    path('login/', auth_views.LoginView.as_view(template_name='myapp/login.html'), name='login_page'),
    path('http://0.0.0.0:8080/realms/my_blog/account//', views.keycloak_login, name='keycloak_login'),
    path('keycloak_callback/', keycloak_callback, name='keycloak_callback'),
    path('oidc/', include('django_keycloak.urls')),
    path('logout/', views.logout, name='logout'),
    path('protected/', views.protected, name='protected'),
]

