from django.urls import path, include
from rest_framework import routers
from .views import (TvSeriesView, ActorsView, DirectorView, 
TvSeriesSeasonView, SeriesActorsView, SeriesTreylerView,
SeriesGenreView)

router = routers.DefaultRouter()
router.register('TvSeries', TvSeriesView, basename='TvSeries')

urlpatterns = [
    path('TvSeries/', include(router.urls)),
    path('Actors/', ActorsView.as_view({'get':'list', 'post': 'create'})),
    path('Directors/', DirectorView.as_view({'get':'list', 'post': 'create'})),
    path('TvSeriesSeason/', TvSeriesSeasonView.as_view()),
    path('SeriesGenre/', SeriesGenreView.as_view()),
    path('SeriesActors/', SeriesActorsView.as_view()),
    path('SeriesActors/', SeriesActorsView.as_view()),
    path('SeriesTreyler/', SeriesTreylerView.as_view()),
]