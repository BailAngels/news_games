from django.db import models


class Tag(models.Model):
    title = models.CharField(
        max_length=100,
        verbose_name="Название",
    )

    def __str__(self):
        return f"{self.title}"

    class Meta:
        verbose_name = "Тег"
        verbose_name_plural = "Теги"
        ordering = ['title']
