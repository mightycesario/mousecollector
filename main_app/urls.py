from django.urls import path
from . import views

urlpatterns = [
  path("", views.home, name="home"),
  path("about/", views.about, name="about"),
  path("mice/", views.mice_index, name="index"),
  path("mice/<int:id>/", views.mice_detail, name="detail"),
  path("mouse/<int:id>/add_photo/", views.add_photo, name="add_photo" ),
]