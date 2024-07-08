from django.db import models
from django_ckeditor_5.fields import CKEditor5Field


class Lesson(models.Model):
    title = models.CharField(max_length=128)
    content = CKEditor5Field(config_name='extends')
    diff_level = models.ForeignKey('DiffLevel', on_delete=models.SET_NULL, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


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
    content = CKEditor5Field(config_name='extends')
    correct_answer = models.CharField(max_length=200)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class DiffLevel(models.Model):
    title = models.CharField(max_length=128)

    def __str__(self):
        return self.title
