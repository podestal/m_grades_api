# Generated by Django 5.0.6 on 2024-05-16 01:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_grades_api', '0010_alter_activity_capacities_alter_activity_competences'),
    ]

    operations = [
        migrations.AddField(
            model_name='quartergrade',
            name='conclusion',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='quartergrade',
            name='competence',
            field=models.CharField(max_length=255),
        ),
    ]
