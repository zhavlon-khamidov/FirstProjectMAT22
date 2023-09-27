from django.urls import path
from firstapp import views

urlpatterns = [
    path('', views.hello, name='home'),
    path('about', views.hello_template, name='template')
]