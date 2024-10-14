from django.urls import path

from .views import LessonListView, study_lesson, d_levels

urlpatterns = [
    path('', LessonListView.as_view(), name="lessons"),
    path('level/<int:level_id>', d_levels, name="levels"),
    path('study/<int:lesson_id>', study_lesson, name="study_lesson"),
]