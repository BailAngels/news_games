from django.contrib import admin

from apps.likes.models import LikeNews, LikeComments


@admin.register(LikeNews)
class LikeNewsAdmin(admin.ModelAdmin):
    list_display = ('user', )
    list_display_links = ('user', )


@admin.register(LikeComments)
class LikeCommentsAdmin(admin.ModelAdmin):
    list_display = ('user', )
    list_display_links = ('user', )


