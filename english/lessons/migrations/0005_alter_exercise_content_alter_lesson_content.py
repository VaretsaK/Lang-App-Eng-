# Generated by Django 5.0.6 on 2024-06-26 20:53

import django_ckeditor_5.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lessons', '0004_alter_lesson_content'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exercise',
            name='content',
            field=django_ckeditor_5.fields.CKEditor5Field(),
        ),
        migrations.AlterField(
            model_name='lesson',
            name='content',
            field=django_ckeditor_5.fields.CKEditor5Field(),
        ),
    ]
