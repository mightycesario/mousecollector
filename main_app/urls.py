from django.urls import path
from . import views

urlpatterns = [
  path("", views.home, name="home"),
  path("about/", views.about, name="about"),
  path("mice/", views.mice_index, name="index"),
  path("mice/<int:mouse_id>/", views.mice_detail, name="detail"),  
  
  # route for the meal dropdrown to work w django form on details page
  path("mice/<int:mouse_id>/add_feeding", views.add_feeding, name="add_feeding"),
  path("mice/<int:mouse_id>/assoc_toy/<int:toy_id>/", views.assoc_toy, name="assoc_toy"),  
  path("accounts/signup/", views.signup, name="signup"),
  # path("mouse/<int:mouse_id>/add_photo/", views.add_photo, name="add_photo" ),
]