from django.db import models

from apps.news.models import News
from django.contrib.auth.models import User


class Comment(models.Model):
    news = models.ForeignKey(
        News,
        on_delete=models.CASCADE,
        verbose_name='Новости',
        related_name='news_comments',
    )
    text = models.TextField(
        max_length=500,
        verbose_name='текст',
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='Автор',
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='дата создания',
    )

    def __str__(self):
        return f'{self.text}'

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарий'
        ordering = ['text']


