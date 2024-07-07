from django.urls import path

from .views import lessons, study_lesson, levels

urlpatterns = [
    path('', lessons, name="lessons"),
    path('level/<int:level_id>', levels, name="levels"),
    path('study/<int:lesson_id>', study_lesson, name="study_lesson"),
]