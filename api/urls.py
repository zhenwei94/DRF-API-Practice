from django.urls import path, include
from rest_framework import routers
from .views import *


router = routers.DefaultRouter()
router.register('books',BookViewSet)
router.register('movies',MovieViewSet)
router.register('authors',AuthorViewSet)
router.register('characters',CharacterViewSet)
router.register('booknumbers',BooknumberViewSet)
router.register(('users'),UserViewSet)
router.register(('ratings'),RatingViewSet)


urlpatterns = [
    path('', include(router.urls)),
]
