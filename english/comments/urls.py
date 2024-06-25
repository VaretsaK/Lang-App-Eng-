from django.urls import path

from .views import comment, add_comment

urlpatterns = [
    path('', comment, name="comment"),
    path('add-comment/', add_comment, name="add_comment"),
]
