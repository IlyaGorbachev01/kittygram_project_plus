from django.urls import include, path

from rest_framework.routers import DefaultRouter
from rest_framework.authtoken import views

from cats.views import CatViewSet, LightCatViewSet, OwnerViewSet


router = DefaultRouter()
router.register('cats', CatViewSet, basename='cat')
router.register('owners', OwnerViewSet)
router.register(r'mycats', LightCatViewSet, basename='mycat')

urlpatterns = [
    path('', include(router.urls)),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),
]
