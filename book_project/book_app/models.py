from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class book(models.Model):
    TYPE = [
        ('Engineering','Engineering'),
        ('Medical','Medical'),
        ('Science fiction','Science fiction'),
        ('PSC','PSC'),
        ('Polictics','Polictics'),
        ('Finance','Finance'),
        ('Fiction','Fiction'),
        ('Ohters','Others')
    ]
    title = models.CharField(max_length = 50)
    author = models.CharField(max_length = 50)
    image = models.ImageField(upload_to='images/')
    price = models.CharField(max_length = 50)
    description = models.TextField()
    category = models.CharField(max_length = 50,choices = TYPE)

class comment(models.Model):
        fk_book = models.ForeignKey(book,on_delete = models.CASCADE)
        fk_user = models.ForeignKey(User,on_delete = models.CASCADE)
        comment = models.CharField(max_length = 50)
