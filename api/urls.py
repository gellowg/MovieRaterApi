from django.contrib import admin
from django.urls import path
from rest_framework import routers
from django.urls.conf import include
from .views import MovieViewset, RatingViewset, UserViewSet

router = routers.DefaultRouter()
router.register('users', UserViewSet)
router.register('movies', MovieViewset)
router.register('ratings', RatingViewset)

urlpatterns = [
    path('', include(router.urls)),
]
