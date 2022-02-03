# Generated by Django 3.2.9 on 2022-02-03 22:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0009_alter_project_expectedlength'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='expectedLength',
            field=models.DurationField(verbose_name='Expected Development Time'),
        ),
        migrations.AlterField(
            model_name='project',
            name='startDate',
            field=models.DateField(blank=True, null=True, verbose_name='Start Date'),
        ),
    ]
