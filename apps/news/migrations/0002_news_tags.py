# Generated by Django 5.0 on 2023-12-26 13:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
        ('tags', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='tags',
            field=models.ManyToManyField(to='tags.tag', verbose_name='Теги'),
        ),
    ]