from django.urls import path
from .views import TreylerView

urlpatterns = [path('treyler/', TreylerView.as_view())]