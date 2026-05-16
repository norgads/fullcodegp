from django.contrib import admin
from .models import Game, Screenshot


class ScreenshotInline(admin.TabularInline):
    model = Screenshot
    extra = 1

class GameAdmin(admin.ModelAdmin):
    list_display = ('title', 'image', 'release_date')
    search_fields = ('title', 'genre', 'developer')
    ordering = ('title',)
    inlines = [ScreenshotInline]

admin.site.register(Game, GameAdmin)

