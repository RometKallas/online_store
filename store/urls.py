from django.urls import path

#Connect the urls to the views
from . import views

app_name = 'store'

urlspatters = [
    path('', views.home, name='home')
]