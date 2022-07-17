from django.urls import path

from .views import IndexView, MatchView, CreateMatchView, UpdateMatchView

urlpatterns = [
    path('', IndexView.as_view()),
    path('all/', MatchView.as_view()),
    path('create/', CreateMatchView.as_view()),
    path('update/<int:id>/', UpdateMatchView.as_view()),
]
