from django.contrib import admin

from apps.games.models import Game


@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    list_display = ('title', )
    list_display_links = ('title', )
    search_fields = ('title', )
    list_filter = ('genres', 'publisher')
