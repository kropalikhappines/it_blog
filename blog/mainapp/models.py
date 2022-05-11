import email
from django.db import models
from birthday import BirthdayField, BirthdayManager

# Create your models here.


class Author(models.Model):
    author_id = models.AutoField(primary_key=True)
    first_name_author = models.CharField(max_length=64)
    last_name_author = models.CharField(max_length=64)
    username_author = models.CharField(max_length=64, unique=True)
    birthday_author = BirthdayField()
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    email_author = models.EmailField(unique=True)