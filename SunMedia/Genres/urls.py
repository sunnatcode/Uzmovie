from django.urls import path
from .views import *
urlpatterns = [
    path('Genres/', GenreView.as_view({
        'post':'create',
        'get':'list'
    }))
]