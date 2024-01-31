# Generated by Django 4.1.3 on 2024-01-31 01:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('itineraryapi', '0005_alter_tripactivity_trip'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tripactivity',
            name='trip',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='activity_trips', to='itineraryapi.trip'),
        ),
    ]