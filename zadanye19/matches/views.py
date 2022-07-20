from django.shortcuts import render
from django.views import View
from django.views.generic import ListView
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

from .models import Match

class IndexView(ListView):
    queryset = Match.objects.all()
    context_object_name = 'matches'
    template_name = 'index.html'

class MatchView(ListView):
    queryset = Match.objects.all()
    context_object_name = 'matches'
    template_name = 'matches.html'

class CreateMatchView(View):
    def get(self, request):
        return render(request, 'create.html')

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super(CreateMatchView, self).dispatch(request, *args, **kwargs)

    def post(self, request):
        Match.objects.create(
            first_team=request.POST['deposit'],
            second_team=request.POST['deposit'],
            description=request.POST['description'],
            stadium=request.POST['stadium'],
            start_date=request.POST['start_date'],
        )
        return render(request, 'create.html')

class UpdateMatchView(View):
    def get(self, request, id):
        match = Match.objects.get(id=id)
        data = {'match': match}
        return render(request, 'update.html', data)

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super(UpdateMatchView, self).dispatch(request, *args, **kwargs)

    def post(self, request, id):
        match = Match.objects.get(id=id)
        match.description = request.POST['description']
        match.start_date = request.POST['start_date']
        match.save()
        data = {'match': match}
        return render(request, 'update.html', data)
