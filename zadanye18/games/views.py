from django.shortcuts import render

from .models import Game

# Create your views here.
def index(request):
    return render(request, 'index.html')

def all_games(request):
    games = Game.objects.all()
    data = {'games': games}
    return render(request, 'games.html', data)

def rules(request):
    return render(request, 'rules.html')