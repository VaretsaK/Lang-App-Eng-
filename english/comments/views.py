from django.shortcuts import render, redirect
from comments.models import Comment
from comments.forms import CommentForm
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy


class CommentListView(ListView):
    model = Comment
    template_name = 'comments/comments.html'
    context_object_name = 'comments'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'All comments'
        return context


class AddCommentCreateView(CreateView):
    model = Comment
    form_class = CommentForm
    template_name = 'comments/create_comment.html'

    def get_success_url(self):
        return reverse_lazy('comment')


class EditCommentUpdateView(UpdateView):
    model = Comment
    form_class = CommentForm
    template_name = 'comments/edit_comment.html'

    def get_success_url(self):
        return reverse_lazy('comment')


class DeleteCommentDeleteView(DeleteView):
    model = Comment
    template_name = 'comments/delete_comment.html'

    def get_success_url(self):
        return reverse_lazy('comment')