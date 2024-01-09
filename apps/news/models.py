from django.db import models

from apps.games.models import Game
from django.contrib.auth.models import User
from apps.tags.models import Tag


class News(models.Model):
    title = models.CharField(
        max_length=100,
        verbose_name='Навание',
    )
    description = models.TextField(
        verbose_name='описание',
    )
    image = models.ImageField(
        verbose_name='Фото',
        upload_to='news_img/',
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата создания',
    )
    game = models.ForeignKey(
        Game,
        on_delete=models.CASCADE,
        verbose_name='Игра',
    )
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='Автор',
    )
    tags = models.ManyToManyField(
        Tag,
        verbose_name='Теги'
    )



    def __str__(self):
        return f'{self.title}'

    def get_summ_like(self):
        return sum([1 for i in self.likes.all()])

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
        ordering = ['title']
