from django.urls import path

from .views import lessons

urlpatterns = [
    path('', lessons, name="index"),
]