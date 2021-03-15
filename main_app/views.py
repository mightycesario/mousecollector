from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Mouse, Toy
from .forms import FeedingForm
import uuid
import boto3




# Create your views here.
def home(request):
  return render(request, "about.html")

def about(request):
  return render(request, "about.html")

def mice_index(request):
  mice = Mouse.objects.all()
  return render(request, "mice/index.html", { "mice": mice })


def mice_detail(request, mouse_id):
  mouse = Mouse.objects.get(id=mouse_id)
  toys_mouse_doesnt_have = Toy.objects.exclude(id__in = mouse.toys.all().values_list("id"))
  # instantiate FeedingForm to be rendered in the template
  feeding_form = FeedingForm()
  # include the mouse and feeding_form in the context
  context = {
    "mouse": mouse,
    "feeding_form": feeding_form,
    "toys": toys_mouse_doesnt_have
  }
  return render(request, "mice/detail.html", context)  


def assoc_toy(request, mouse_id, toy_id):
  Mouse.objects.get(id=mouse_id).toys.add(toy_id)
  return redirect("detail", mouse_id=mouse_id)  
  

def add_feeding(request, mouse_id):
  form = FeedingForm(request.POST)
  # validate the form from the backend
  if form.is_valid():
    # dont save the form to the db until it
    # has the mouse_id assgined
    # create an instance of the feeding but doesnt save to db
    new_feeding = form.save(commit=False)
    # add mouse id to the feeding
    new_feeding.mouse_id = mouse_id
    # save the feeding to the db
    new_feeding.save()
  # using redirect instead of render 
  # if data has been changed in the database.
  return redirect("detail", mouse_id=mouse_id)















