from django.urls import path, include
from remembers.views import main

urlpatterns = [
    path('', main)
]