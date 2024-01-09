from django.contrib.auth.models import User
from django.db import models

from apps.news.models import News
from apps.comments.models import Comment


class LikeNews(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='Автор',
    )
    count = models.IntegerField(
        default=1,
    )
    news = models.ForeignKey(
        News,
        on_delete=models.CASCADE,
        verbose_name='Новость',
        related_name='news_likes',
    )

    def __str__(self):
        return f'{self.user.username}'

    class Meta:
        verbose_name = 'Лайк новости'
        verbose_name_plural = 'Лайк новостям'


class LikeComments(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='Автор',
    )
    count = models.IntegerField(
        default=1,
    )
    comment = models.ForeignKey(
        Comment,
        on_delete=models.CASCADE,
        verbose_name='Комментарий',
        related_name='comment_likes',
    )

    def __str__(self):
        return f'{self.user.username}'

    class Meta:
        verbose_name = 'Лайк комментария'
        verbose_name_plural = 'Лайк комментариев'


