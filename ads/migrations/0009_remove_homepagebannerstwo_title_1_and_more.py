# Generated by Django 5.0.1 on 2024-05-06 12:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ads', '0008_homepagebannerstwo_link'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='homepagebannerstwo',
            name='title_1',
        ),
        migrations.RemoveField(
            model_name='homepagebannerstwo',
            name='title_2',
        ),
        migrations.RemoveField(
            model_name='homepagebannerstwo',
            name='title_3',
        ),
    ]
