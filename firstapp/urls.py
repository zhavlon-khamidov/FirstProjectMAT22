from django.urls import path
from firstapp.views import hello

urlpatterns = [
    path('', hello)
]