# Generated by Django 4.2.1 on 2024-03-11 10:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Studet',
            fields=[
                ('roll', models.IntegerField(primary_key=True, serialize=False)),
                ('sname', models.CharField(max_length=50)),
                ('add', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
    ]
