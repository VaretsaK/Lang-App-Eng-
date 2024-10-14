from django.urls import path

from .views import LessonListView, LessonDetailView, d_levels

urlpatterns = [
    path('', LessonListView.as_view(), name="lessons"),
    path('level/<int:level_id>', d_levels, name="levels"),
    path('study/<int:pk>', LessonDetailView.as_view(), name="study_lesson"),
]