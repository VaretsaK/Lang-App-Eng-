from django.urls import path

from .views import CommentListView, AddCommentCreateView

urlpatterns = [
    path('', CommentListView.as_view(), name="comment"),
    path('add-comment/', AddCommentCreateView.as_view(), name="add_comment"),
]
