from django.urls import path, include
from .views import *
from rest_framework import routers
from rest_framework import renderers
router = routers.DefaultRouter()
router.register('Movie', MovieView, basename='Movie')
router.register('Movie', MovieActorView, basename='MovieActor')




urlpatterns = [
    path('Director/', DirectorView.as_view({
        'post':'create',
        'get':'list'
    })),



    path('Movie/', include(router.urls)),
    

    path('Actors/', ActorsView.as_view({
        'post':'create',
        'get':'list'
    })),

    path('MovieActors/', include(router.urls)),


    path('MovieGenre/', MovieGenreView.as_view({
        'post':'create',
        'get':'list'
    })),



]