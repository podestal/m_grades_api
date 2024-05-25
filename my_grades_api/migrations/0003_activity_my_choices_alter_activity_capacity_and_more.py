# Generated by Django 5.0.6 on 2024-05-14 16:36

import multiselectfield.db.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_grades_api', '0002_remove_activity_capacity_remove_activity_competence_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='activity',
            name='my_choices',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('item_key1', 'Item title 1.1'), ('item_key2', 'Item title 1.2'), ('item_key3', 'Item title 1.3'), ('item_key4', 'Item title 1.4'), ('item_key5', 'Item title 1.5')], default=1, max_length=10),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='activity',
            name='capacity',
            field=models.ManyToManyField(related_name='capacities', to='my_grades_api.capacity'),
        ),
        migrations.AlterField(
            model_name='activity',
            name='competence',
            field=models.ManyToManyField(related_name='competences', to='my_grades_api.competence'),
        ),
    ]
