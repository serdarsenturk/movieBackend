# Generated by Django 3.0.4 on 2020-06-05 17:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0007_actor_surname'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='actor',
            name='created',
        ),
    ]