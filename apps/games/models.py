from django.db import models
from apps.genres.models import Genre
from apps.publishers.models import Publisher


class Game(models.Model):
    title = models.CharField(
        max_length=120,
        verbose_name='Название',
    )
    description = models.TextField(
        verbose_name='Описание',
    )
    image = models.ImageField(
        verbose_name='Фото',
        upload_to='games_img/',
    )
    relise_date = models.DateField(
        verbose_name='Дата выхода',
    )
    price = models.DecimalField(
        verbose_name='Цена',
        max_digits=6,
        decimal_places=2,
    )
    publisher = models.ForeignKey(
        Publisher,
        on_delete=models.CASCADE,
        verbose_name='Издатель',
    )
    genres = models.ManyToManyField(
        Genre,
        verbose_name='Жанры',
    )

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'Игра'
        verbose_name_plural = 'Игры'
        ordering = ['title']
