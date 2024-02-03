# Generated by Django 4.1.3 on 2024-02-03 18:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('itineraryapi', '0010_alter_trip_destination_delete_destination'),
    ]

    operations = [
        migrations.CreateModel(
            name='ActivityReview',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('review', models.TextField(max_length=150)),
                ('activity', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='itineraryapi.activity')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='activity_reviews', to='itineraryapi.admin')),
            ],
        ),
    ]
