from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_picture = models.ImageField(upload_to="users/profile_pictures", null=True, blank=True)

    def __str__(self):
        return self.user.username


class UserExerciseAttempt(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    exercise = models.ForeignKey('lessons.Exercise', on_delete=models.CASCADE)
    is_correct = models.BooleanField()
    attempt_date = models.DateTimeField(auto_now_add=True)
