"""Администрирование моделей Post, Group и Comment."""

from django.contrib import admin
from .models import Comment, Group, Post


class PostAdmin(admin.ModelAdmin):
    """Админ настройки для модели Post."""

    list_display = ('pk', 'text', 'pub_date', 'author')
    search_fields = ('text',)
    list_filter = ('pub_date',)
    empty_value_display = '-пусто-'


admin.site.register(Post, PostAdmin)
admin.site.register(Group)
admin.site.register(Comment)
