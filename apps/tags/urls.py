from django.urls import path

from apps.tags.views import list_tags, news_in_tags

urlpatterns = [
    path('tags/', list_tags, name='list_tags'),
    path('tags/<str:title>', news_in_tags, name='news_in_tags'),
]