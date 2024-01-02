
from django.urls import path

#from . import views
from .views import api01_home, api02_home

urlpatterns = [
    path('01/', api01_home,  name="api01-home"),
    path('02/', api02_home,  name="api02-home"),
    
]
