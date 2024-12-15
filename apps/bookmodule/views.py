from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
# from .models import Book,Author
# Create your views here.
def index(request): 
    return HttpResponse("Hello, world!")


def Landing_Page(request): 
    return render(request, "home.html" ) 


