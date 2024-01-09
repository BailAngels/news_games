from django.shortcuts import render

from apps.tags.models import Tag
from apps.news.models import News


def list_tags(request):
    tag = Tag.objects.all()

    context = {
        'tag': tag,
    }
    return render(request, 'tags/list_tags.html', context=context)


def news_in_tags(request, title):
    tags = Tag.objects.all()
    right_news = News.objects.all().order_by('-created_at')[:3]
    tag = Tag.objects.get(title=title)
    news = News.objects.filter(tags=tag)
    if request.method == 'POST':
        news = News.objects.filter(title__icontains=request.POST['search'])
    return render(request, 'news/news.html', locals())
