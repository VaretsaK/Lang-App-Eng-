from django.contrib import admin

from lessons.models import Lesson, Exercise, DiffLevel

admin.site.register(Lesson)
admin.site.register(Exercise)
admin.site.register(DiffLevel)
