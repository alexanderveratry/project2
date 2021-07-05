from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = "listing"
urlpatterns = [
    path("", views.index, name="index"),
    path("<int:listing_id>", views.list, name="listing"),



]