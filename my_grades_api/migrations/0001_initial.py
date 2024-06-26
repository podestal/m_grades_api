# Generated by Django 5.0.6 on 2024-05-09 15:08

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Area',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Clase',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('grade', models.CharField(blank=True, choices=[('1', 'First'), ('2', 'Second'), ('3', 'Third'), ('4', 'Fourth'), ('5', 'Fifth'), ('6', 'Sixth')], max_length=1, null=True)),
                ('level', models.CharField(choices=[('P', 'Primary'), ('S', 'Secondary')], max_length=1)),
                ('section', models.CharField(default='A', max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='School',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Assignature',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('area', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='my_grades_api.area')),
                ('clase', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='assignatures', to='my_grades_api.clase')),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('weight', models.FloatField(blank=True, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='categories', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Annunciation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('created_at', models.DateField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='announcements', to=settings.AUTH_USER_MODEL)),
                ('clase', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='announcements', to='my_grades_api.clase')),
            ],
        ),
        migrations.CreateModel(
            name='Competence',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('area', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='my_grades_api.area')),
            ],
        ),
        migrations.CreateModel(
            name='Capacity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('competence', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='my_grades_api.competence')),
            ],
        ),
        migrations.CreateModel(
            name='Activity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('due_date', models.DateField(blank=True, null=True)),
                ('quarter', models.CharField(choices=[('Q1', 'First Quarter'), ('Q2', 'Second Quarter'), ('Q3', 'Third Quarter'), ('Q4', 'Fourth Quarter')], max_length=2)),
                ('assignature', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='my_grades_api.assignature')),
                ('capacity', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='my_grades_api.capacity')),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='my_grades_api.category')),
                ('competence', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='my_grades_api.competence')),
            ],
        ),
        migrations.CreateModel(
            name='Instructor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(blank=True, max_length=255, null=True)),
                ('last_name', models.CharField(blank=True, max_length=255, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='instructor', to=settings.AUTH_USER_MODEL)),
                ('school', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='instructors', to='my_grades_api.school')),
            ],
        ),
        migrations.AddField(
            model_name='assignature',
            name='Instructor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='assignatures', to='my_grades_api.instructor'),
        ),
        migrations.AddField(
            model_name='clase',
            name='school',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='my_grades_api.school'),
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('clase', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='students', to='my_grades_api.clase')),
                ('school', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='students', to='my_grades_api.school')),
            ],
        ),
        migrations.CreateModel(
            name='QuarterGrade',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('calification', models.CharField(choices=[('AD', 'AD'), ('A', 'A'), ('B', 'B'), ('C', 'C')], max_length=2)),
                ('quarter', models.CharField(choices=[('Q1', 'First Quarter'), ('Q2', 'Second Quarter'), ('Q3', 'Third Quarter'), ('Q4', 'Fourth Quarter')], max_length=2)),
                ('assignature', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='my_grades_api.assignature')),
                ('competence', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='my_grades_api.competence')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='averages', to='my_grades_api.student')),
            ],
        ),
        migrations.CreateModel(
            name='Participation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('calification', models.CharField(choices=[('AD', 'AD'), ('A', 'A'), ('B', 'B'), ('C', 'C')], default='NA', max_length=2)),
                ('observations', models.TextField(blank=True, null=True)),
                ('created_at', models.DateField(auto_now_add=True)),
                ('assignature', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='my_grades_api.assignature')),
                ('capacity', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='my_grades_api.capacity')),
                ('competence', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='my_grades_api.competence')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='participations', to='my_grades_api.student')),
            ],
        ),
        migrations.CreateModel(
            name='Grade',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('calification', models.CharField(choices=[('NA', 'NA'), ('AD', 'AD'), ('A', 'A'), ('B', 'B'), ('C', 'C')], default='NA', max_length=2)),
                ('created_at', models.DateField(auto_now_add=True)),
                ('observations', models.TextField(blank=True, null=True)),
                ('activity', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='grades', to='my_grades_api.activity')),
                ('assignature', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='grades', to='my_grades_api.assignature')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='grades', to='my_grades_api.student')),
            ],
        ),
        migrations.CreateModel(
            name='Atendance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateField(auto_now_add=True)),
                ('status', models.CharField(choices=[('L', 'Late'), ('N', 'Not Attended')], max_length=1)),
                ('hour', models.TimeField(blank=True, null=True)),
                ('created_by', models.CharField(max_length=255)),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='atendances', to='my_grades_api.student')),
            ],
        ),
        migrations.CreateModel(
            name='Tutor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(blank=True, max_length=255, null=True)),
                ('last_name', models.CharField(blank=True, max_length=255, null=True)),
                ('school', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tutors', to='my_grades_api.school')),
                ('students', models.ManyToManyField(related_name='tutors', to='my_grades_api.student')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
