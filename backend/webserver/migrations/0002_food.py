# Generated by Django 5.0.6 on 2024-05-24 05:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webserver', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Food',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.TextField()),
                ('Calories', models.TextField()),
                ('Carbohydrates', models.TextField()),
                ('Proteins', models.TextField()),
                ('Fat', models.TextField()),
                ('Fiber', models.TextField()),
            ],
        ),
    ]
