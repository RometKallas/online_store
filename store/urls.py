from django.urls import path

#Connect the urls to the views
from . import views

app_name = 'store'

urlpatterns = [
    path('', views.homepage, name='homepage')
]