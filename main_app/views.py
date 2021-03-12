from django.shortcuts import render
from django.http import HttpResponse


# create the mouse class 
class Mouse:
  def __init__(self, name, species, description, age):
    self.name = name
    self.species = species
    self.description = description
    self.age = age

mice = [
  Mouse("Eek", "white mouse", "chubby yet fast white mouse with brown spots", 2),
  Mouse("Phoebe", "house mouse", "loud and likes to run around", 1),
  Mouse("Cheeks", "deer mouse", "small and quiet", 4)
]

# Create your views here.
def home(request):
  return HttpResponse('<h1>Mouse! /ᐠ｡‸｡ᐟ\ﾉ</h1>')

def about(request):
  return render(request, "about.html")

def mice_index(request):
  return render(request, "mice/index.html", { "mice": mice })