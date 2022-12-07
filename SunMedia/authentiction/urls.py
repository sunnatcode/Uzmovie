from django.urls import path
from .views import *

urlpatterns = [
    path('auth_create/', RegisterView.as_view()),
    path('auth_get/', RegisterGetView.as_view()),
    path('auth_delete/<int:pk>/', UserDelete.as_view()),

    path('login/', LoginApiView.as_view()),
]