# Generated by Django 3.2.13 on 2022-05-11 12:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('mainapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id_article', models.AutoField(primary_key=True, serialize=False)),
                ('name_article', models.CharField(max_length=128)),
                ('text_article', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
                ('author_article', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='mainapp.author')),
            ],
        ),
    ]
