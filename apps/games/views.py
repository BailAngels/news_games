from django.shortcuts import render, redirect

from apps.games.models import Game
from apps.tags.models import Tag
from apps.genres.models import Genre
from apps.news.models import News


def list_games(request):
    games = Game.objects.all()
    genres = Genre.objects.all()
    if request.method == 'POST':
        game = Game.objects.filter(title__icontains=request.POST['search'])
    return render(request, 'games/games.html', locals())


def detail_game(request, pk):
    game = Game.objects.get(id=pk)
    genres = Genre.objects.all()
    return render(request, 'games/game.html', locals())


def games_in_genres(request, title):
    right_genres = Genre.objects.all()
    genre = Genre.objects.get(title=title)
    games = Game.objects.filter(genres=genre)
    if request.method == 'POST':
        games = Game.objects.filter(title__icontains=request.POST['search'])
    return render(request, 'games/games.html', locals())