from django.shortcuts import render
from django.http import HttpResponseNotFound
from lessons.models import Lesson, Exercise, DiffLevel
from django.views.generic import ListView, DetailView


class LessonListView(ListView):
    model = Lesson
    template_name = 'lessons/all_lessons_page.html'
    context_object_name = 'lessons'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['levels'] = DiffLevel.objects.all()
        context['title'] = 'List of lessons'
        return context


class LessonDetailView(DetailView):
    model = Lesson
    template_name = 'lessons/lesson.html'
    context_object_name = 'lesson'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['exercises'] = Exercise.objects.filter(lesson=self.object)
        context['title'] = 'Study the lesson'
        return context


def d_levels(request, level_id):
    filtered_lessons = Lesson.objects.filter(diff_level__id=level_id)
    levels = DiffLevel.objects.all()
    context = {
        'lessons': filtered_lessons,
        'title': 'List of lessons by level',
        'levels': levels
    }
    return render(request, 'lessons/lessons_level.html', context)
