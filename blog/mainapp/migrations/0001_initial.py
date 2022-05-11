# Generated by Django 3.2.13 on 2022-05-11 11:48

import birthday.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('author_id', models.AutoField(primary_key=True, serialize=False)),
                ('first_name_author', models.CharField(max_length=64)),
                ('last_name_author', models.CharField(max_length=64)),
                ('username_author', models.CharField(max_length=64, unique=True)),
                ('birthday_author_dayofyear_internal', models.PositiveSmallIntegerField(default=None, editable=False, null=True)),
                ('birthday_author', birthday.fields.BirthdayField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
                ('email_author', models.EmailField(max_length=254, unique=True)),
            ],
        ),
    ]
