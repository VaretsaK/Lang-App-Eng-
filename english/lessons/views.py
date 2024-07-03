from django.shortcuts import render
from django.http import HttpResponseNotFound
from lessons.models import Lesson, Exercise


def lessons(request):
    all_lessons = Lesson.objects.all()
    context = {
        'lessons': all_lessons,
        'title': 'List of lessons'
    }
    return render(request, 'lessons/all_lessons_page.html', context)


def study_lesson(request, lesson_id):

    try:
        lesson_to_study = Lesson.objects.get(pk=lesson_id)
    except Lesson.DoesNotExist:
        return HttpResponseNotFound()

    exercises_for_lesson = Exercise.objects.filter(lesson=lesson_to_study)
    context = {
        'lesson': lesson_to_study,
        'title': 'Study the lesson',
        'exercises': exercises_for_lesson,
    }
    return render(request, 'lessons/lesson.html', context)
