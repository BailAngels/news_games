from django.urls import path

from apps.genres.views import list_genres

urlpatterns = [
    path('list_genres/', list_genres, name='list_genres')
]

