from django.urls import path
from .views import index, all_games, rules

urlpatterns = [
    path('', index),
    path('all', all_games),
    path('rules', rules)
]