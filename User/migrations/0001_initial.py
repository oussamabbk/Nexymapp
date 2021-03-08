# Generated by Django 3.1.7 on 2021-03-08 09:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nom', models.CharField(max_length=255)),
                ('Prenom', models.CharField(max_length=255)),
                ('mobile', models.IntegerField()),
                ('picture', models.CharField(max_length=255)),
                ('Email', models.CharField(max_length=255)),
                ('password', models.CharField(max_length=255)),
                ('datedenaisance', models.DateTimeField(auto_now_add=True)),
                ('adresse', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('sexe', models.CharField(max_length=255)),
                ('statue', models.BooleanField()),
            ],
        ),
    ]
