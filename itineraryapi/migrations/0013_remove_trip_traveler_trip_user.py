# Generated by Django 4.1.3 on 2024-02-09 03:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('itineraryapi', '0012_secretreview'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='trip',
            name='traveler',
        ),
        migrations.AddField(
            model_name='trip',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='itineraryapi.admin'),
        ),
    ]