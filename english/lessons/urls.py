from django.urls import path

from .views import lessons, study_lesson

urlpatterns = [
    path('', lessons, name="lessons"),
    path('study/<int:lesson_id>', study_lesson, name="study_lesson"),
]