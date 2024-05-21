from django.urls import path, include
from .views import main


app_name = 'remembers'

urlpatterns = [
    path('', main, name='main')
]