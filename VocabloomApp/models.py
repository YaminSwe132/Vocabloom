from django.db import models

# Create your models here.

#topic
class Topic(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=500)

#word
class Word(models.Model):
    word = models.CharField(max_length=100)
    phonetic_sign = models.CharField(max_length=100, blank=True, null=True)
    defination = models.CharField(max_length=200)
    example_sentence = models.CharField(max_length=200)
