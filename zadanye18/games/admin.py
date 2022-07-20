from django.contrib import admin

from .models import Game
# Register your models here.
class GameAdmin(admin.ModelAdmin):
    list_display = (
        'pk',
        'deposit',
        'game_type',
        'start_date',
        'end_date',
    )

admin.site.register(Game, GameAdmin)