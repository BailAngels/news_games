from django.contrib import admin

from apps.publishers.models import Publisher


@admin.register(Publisher)
class PublisherAdmin(admin.ModelAdmin):
    list_display = ('title', )
    list_display_links = ('title', )
    search_fields = ('title', )