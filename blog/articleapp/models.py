from django.db import models
from django.forms import CharField
from mainapp.models import Author
# Create your models here.


class Article(models.Model):
    id_article = models.AutoField(primary_key=True)
    author_article = models.ForeignKey(Author, on_delete=models.CASCADE)
    name_article = models.CharField(max_length=128)
    text_article = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    