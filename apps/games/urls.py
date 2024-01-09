from django.urls import path

from apps.games.views import list_games, detail_game, games_in_genres

urlpatterns = [
    path('games/', list_games, name='list_games'),
    path('games/<int:pk>', detail_game, name='detail_game'),
    path('games/<str:title>', games_in_genres, name='games_in_genres'),
]