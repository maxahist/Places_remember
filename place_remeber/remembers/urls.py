from django.urls import path, include
from .views import main, remember_edit, remember_create


app_name = "remembers"

urlpatterns = [
    path("main/", main, name="main"),
    path("remember_edit/<int:remember_id>/", remember_edit, name="remember_edit"),
    path("remember_create/", remember_create, name="remember_create"),
    # path('', include('rest_framework_social_oauth2.urls')),
]
