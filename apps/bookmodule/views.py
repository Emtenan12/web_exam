from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from .models import Game,Devolper
# Create your views here.
def index(request): 
    return HttpResponse("Hello, world!")


def Landing_Page(request): 
    return render(request, "home.html" ) 


def list_games(request): 
    games=Game.objects.all()
    return render(request, "list_games.html",{'games':games} ) 