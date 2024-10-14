from django.urls import path

from .views import CommentListView, add_comment

urlpatterns = [
    path('', CommentListView.as_view(), name="comment"),
    path('add-comment/', add_comment, name="add_comment"),
]
