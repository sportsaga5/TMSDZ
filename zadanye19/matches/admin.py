from django.contrib import admin

from .models import Match

class MatchAdmin(admin.ModelAdmin):
    list_display = (
        'pk',
        'first_team',
        'second_team',
        'stadium',
        'start_date',
    )

admin.site.register(Match, MatchAdmin)
