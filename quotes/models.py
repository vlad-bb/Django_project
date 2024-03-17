from django.db import models

# Create your models here. 

class Author(models.Model):
    fullname = models.CharField(max_length=50)
    date_born= models.CharField(max_length=50)
    location_born= models.CharField(max_length=150)
    bio= models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)


class Tag(models.Model):
    name = models.CharField(max_length=100, null=False, unique=True)


class Quote(models.Model):
    quote = models.TextField()
    tags = models.ManyToManyField(Tag)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, default=None, null=True)
    created_at = models.DateTimeField(auto_now_add=True)