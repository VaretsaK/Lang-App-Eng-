from django.shortcuts import render
from django.http import HttpResponseNotFound
from lessons.models import Lesson, Exercise, DiffLevel


def lessons(request):
    all_lessons = Lesson.objects.all()
    levels = DiffLevel.objects.all()
    context = {
        'lessons': all_lessons,
        'title': 'List of lessons',
        'levels': levels
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


def levels(request, level_id):
    filtered_lessons = Lesson.objects.filter(diff_level__id=level_id)
    levels = DiffLevel.objects.all()
    context = {
        'lessons': filtered_lessons,
        'title': 'List of lessons by level',
        'levels': levels
    }
    return render(request, 'lessons/lessons_level.html', context)
