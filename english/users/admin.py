from django.contrib import admin

from users.models import UserProfile, UserExerciseAttempt, PhoneNumber

admin.site.register(UserProfile)
admin.site.register(UserExerciseAttempt)
admin.site.register(PhoneNumber)
