from django.urls import path

#Connect the urls to the views
from . import views

app_name = 'store'

urlpatterns = [
    path('', views.homepage, name='homepage'),
    #first slug is the type of data the second slug is the variable
    path('item/<slug:slug>/', views.product_detail, name='product_detail'),
    path('search/<slug:category_slug>/', views.category_list, name='category_list')
]