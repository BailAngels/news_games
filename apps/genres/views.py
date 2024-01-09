from django.shortcuts import render

from apps.games.models import Game
from apps.genres.models import Genre


def list_genres(request):
    genres = Genre.objects.all()

    context = {
        'genres': genres
    }
    return render(request, 'genres/list_genres.html', context=context)


