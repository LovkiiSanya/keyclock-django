from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'blogs', views.BlogViewSet, basename='blog')
router.register(r'comments', views.CommentViewSet)

urlpatterns = [
    path('', views.home, name='home'),
    path('', include(router.urls)),
]
