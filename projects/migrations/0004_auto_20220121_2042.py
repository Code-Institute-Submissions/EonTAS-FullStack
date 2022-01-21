# Generated by Django 3.2.9 on 2022-01-21 20:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0003_remove_project_image_url'),
    ]

    operations = [
        migrations.RenameField(
            model_name='project',
            old_name='owner',
            new_name='suggester',
        ),
        migrations.AddField(
            model_name='project',
            name='payed_for',
            field=models.BooleanField(default=False),
        ),
    ]
