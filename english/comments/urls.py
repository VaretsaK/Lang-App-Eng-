from django.urls import path

from .views import CommentListView, AddCommentCreateView, EditCommentUpdateView, DeleteCommentDeleteView

urlpatterns = [
    path('', CommentListView.as_view(), name="comment"),
    path('add-comment/', AddCommentCreateView.as_view(), name="add_comment"),
    path('edit-comment/<int:pk>', EditCommentUpdateView.as_view(), name="edit_comment"),
    path('delete-comment/<int:pk>', DeleteCommentDeleteView.as_view(), name="delete_comment"),
]
