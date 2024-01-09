from django.shortcuts import render, redirect

from apps.games.models import Game
from apps.news.models import News
from apps.tags.models import Tag
from apps.genres.models import Genre
from django.contrib.auth.models import User


def list_news(request):
    news = News.objects.all().order_by('-created_at')
    right_news = News.objects.all().order_by('-created_at')[:3]
    tags = Tag.objects.all()
    genres = Genre.objects.all()
    if request.method == 'POST':
        news = News.objects.filter(title__icontains=request.POST['search'])
    return render(request, 'news/news.html', locals())


def detail_news(request, pk):
    right_news = News.objects.all().order_by('-created_at')[:3]
    tags = Tag.objects.all()
    genres = Genre.objects.all()
    try:
        new = News.objects.get(id=pk)
    except News.DoesNotExist:
        return render(request, 'news/notfound.html', locals())
    if request.method == 'POST':
        news = News.objects.filter(title__icontains=request.POST['search'])
    return render(request, 'news/news_detail.html', locals())


def create_news(request):
    tags = Tag.objects.all()
    if request.method == 'POST':
        title = request.POST['title']
        description = request.POST['description']
        image = request.FILES['image']
        tags = request.POST['tags']
        user = request.POST['user']
        games = request.POST['games']

        post_obj = News.objects.create(
            title=title,
            description=description,
            image=image,
            author=user,
            games=games,
        )
        post_obj.game.title()
        return redirect('list_news')

    return render(request, 'news/create_news.html', locals())


def delete_news(request, pk):
    try:
        news = News.objects.get(id=pk)
    except News.DoesNotExist:
        ...

    if news is not None:
        news.delete()
        return redirect('news')
    else:
        return redirect('news')


def edit_news(request, pk):
    news_edit = News.objects.get(id=pk)

    if request.method == 'POST':
        news_edit.title = request.POST['title']
        news_edit.description = request.POST['description']
        news_edit.image = request.FILES['image']
        news_edit.tags = request.POST['tags']
        news_edit.author = request.POST['author']
        news_edit.games = request.POST['games']

        return redirect('list_news')

    return render(request, 'news/edit_news.html', locals())
