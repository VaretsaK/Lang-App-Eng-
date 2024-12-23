# Generated by Django 5.0.6 on 2024-07-07 22:10

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lessons', '0005_alter_exercise_content_alter_lesson_content'),
    ]

    operations = [
        migrations.CreateModel(
            name='DiffLevel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128)),
            ],
        ),
        migrations.AddField(
            model_name='lesson',
            name='diff_level',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='lessons.difflevel'),
        ),
    ]
