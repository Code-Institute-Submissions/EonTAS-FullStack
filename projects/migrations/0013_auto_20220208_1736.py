# Generated by Django 3.2.9 on 2022-02-08 17:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0012_auto_20220204_2100'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='header',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='update',
            name='header',
            field=models.CharField(max_length=255),
        ),
    ]
