from django.shortcuts import render
from django.http import HttpResponse
from .models import Mouse, Photo
import uuid
import boto3



S3_BASE_URL = "https://s3.us-west-1.amazonaws.com/"
BUCKET = "mousecollector-sei0119"


def add_photo(request, id):
  # photo-file will be the name attribute on the <input type="file" name="photo-file">
  photo_file = request.FILES.get("photo-file", None)
  if photo_file:
    # initializing a API to connect to s3
    s3 = boto3.client("s3")
    # we need a unique key for s3 as well as a file extension
    key = uuid.uuid4().hex[:6] + photo_file.name[photo_file.name.rFind('.'):]
    # just in case something goes wrong...
    try:
      # upload the file to s3
      s3.upload_fileobj[photo_file, BUCKET, key]
      # build the URL to the file to save locally in postgres
      url = f" {S3_BASE_URL}{BUCKET}/{key} "
      # create an instance of the photo model
      photo = Photo(url=url, id=id)
      photo.save()
    except:
      print("An error occured uploading the file to s3")
  return redirect("detail", id=id)



# Create your views here.
def home(request):
  return HttpResponse('<h1>Mouse! /ᐠ｡‸｡ᐟ\ﾉ</h1>')

def about(request):
  return render(request, "about.html")

def mice_index(request):
  mice = Mouse.objects.all()
  return render(request, "mice/index.html", { "mice": mice })


def mice_detail(request, mouse_id):
  mouse = Mouse.objects.get(id=mouse_id)
  return render(request, "mice/detail.html", { "mouse": mouse })  