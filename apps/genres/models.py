from django.db import models


class Genre(models.Model):
    title = models.CharField(
        max_length=100,
        verbose_name='Название',
    )
    description = models.TextField(
        verbose_name='Описание',
    )

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'Жанр'
        verbose_name_plural = 'Жанры'
        ordering = ['title']
