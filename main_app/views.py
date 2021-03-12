from django.shortcuts import render
from .models import Mouse

# Create your views here.
def home(request):
  return HttpResponse('<h1>Mouse! /ᐠ｡‸｡ᐟ\ﾉ</h1>')

def about(request):
  return render(request, "about.html")

def mice_index(request):
  return render(request, "mice/index.html", { "mice": mice })