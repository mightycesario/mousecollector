from django.shortcuts import render
from .models import Mouse
import uuid
import boto3


# Create your views here.
def home(request):
  return HttpResponse('<h1>Mouse! /ᐠ｡‸｡ᐟ\ﾉ</h1>')

def about(request):
  return render(request, "about.html")

def mice_index(request):
  mice = Mouse.objects.all()
  return render(request, "mice/index.html", { "mice": mice })


def mice_detail(request, id):
  mouse = Mouse.objects.get(id=id)
  return render(request, "mice/detail.html", { "mouse": mouse })  