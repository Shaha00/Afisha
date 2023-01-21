from django.db import models

# Create your models here.


class Director(models.Model):
    name = models.TextField(null=True, blank=True)


class Movie(models.Model):
    title = models.CharField(max_length=180)
    description = models.TextField()
    duration = models.TextField()
    director = models.ForeignKey(Director, on_delete=models.CASCADE, null=True)


class Review(models.Model):
    text = models.TextField(null=True, blank=True)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, null=True)

