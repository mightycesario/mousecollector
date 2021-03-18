from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Mouse, Toy
from .forms import FeedingForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
import uuid
# import boto3




# Create your views here.
def home(request):
  return render(request, "about.html")

def about(request):
  return render(request, "about.html")

def mice_index(request):
  # helper method to get all mice from DB
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


def signup(request):
  error_message = ""
  if request.method == "POST":
    # This is how to create a "user" form object
    # that includes the data from the browser
    form = UserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user)
      return redirect("index")
    else:
      error_message = "Invalid sign up - try again"
  form = UserCreationForm()
  context = { "form": form, "error_message": error_message}
  return render(request, "registration/signup.html", context)












