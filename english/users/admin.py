from django.contrib import admin

from users.models import UserProfile, UserExerciseAttempt

admin.site.register(UserProfile)
admin.site.register(UserExerciseAttempt)
