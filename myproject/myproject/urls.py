from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from myapp import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

router = DefaultRouter()
router.register(r'blogs', views.BlogViewSet, basename='blog')
router.register(r'comments', views.CommentViewSet, basename='comment')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('oidc/', include('django_keycloak.urls')),
    path('', views.home, name='home_page'),
    path('login/', views.login_page, name='login_page'),
    path('http://0.0.0.0:8080/realms/my_blog/account//', views.keycloak_login, name='keycloak_login'),
    path('keycloak_callback/', views.keycloak_callback, name='keycloak_callback'),
    path('api/', include(router.urls)),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('logout/', views.logout, name='logout'),

]

