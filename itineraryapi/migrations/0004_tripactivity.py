# Generated by Django 4.1.3 on 2024-01-31 00:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('itineraryapi', '0003_traveler_trip'),
    ]

    operations = [
        migrations.CreateModel(
            name='TripActivity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('activity', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='itineraryapi.activity')),
                ('trip', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='itineraryapi.traveler')),
            ],
        ),
    ]
