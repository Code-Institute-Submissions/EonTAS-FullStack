# Generated by Django 3.2.9 on 2022-01-30 17:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0006_auto_20220129_1547'),
        ('checkout', '0010_commission_stripe_pid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='commission',
            name='commItem',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='projects.project'),
        ),
    ]
