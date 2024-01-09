from django.db import models


class Publisher(models.Model):
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
        verbose_name = 'Издатель'
        verbose_name_plural = 'Издатели'
        ordering = ['title']

