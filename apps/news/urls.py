from django.urls import path

from apps.news.views import (
    list_news,
    detail_news,
    create_news,
    delete_news,
    edit_news,
)


urlpatterns = [
    path('', list_news, name='news'),
    path('news/<int:pk>', detail_news, name='detail_news'),
    path('create/', create_news, name='create_news'),
    path('delete/<int:pk>', delete_news, name='delete_news'),
    path('edit/<int:pk>', edit_news, name='edit_news'),
]