from django.db import models


class Lesson(models.Model):
    title = models.CharField(max_length=128)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Exercise(models.Model):
    lesson = models.ForeignKey('Lesson', on_delete=models.CASCADE)
    title = models.CharField(max_length=128)

    exercise_type_choices = [
        ('multiple_choice', 'Multiple Choice'),
        ('fill_in_the_blank', 'Fill in the Blank'),
        ('true_false', 'True/False'),
        ('matching', 'Matching'),
    ]
    exercise_type = models.CharField(max_length=20, choices=exercise_type_choices)

    description = models.TextField()
    content = models.TextField()
    correct_answer = models.CharField(max_length=200)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

