from django.db import models


# Create your models here.


class Director(models.Model):
    name = models.TextField(null=True, blank=True)

    @property
    def movie_count(self):
        count = self.movie_count()
        return count


class Movie(models.Model):
    title = models.CharField(max_length=180)
    description = models.TextField()
    duration = models.TextField()
    director = models.ForeignKey(Director, on_delete=models.CASCADE, null=True, related_name='movie_count')

    @property
    def rating(self):
        count = self.movie_reviews.count()
        if count == 0:
            return 0
        total = sum(filter(None, [i.stars for i in self.movie_reviews.all()]))
        return total / count


CHOICES = (
    (1, 1),
    (2, 2),
    (3, 3),
    (4, 4),
    (5, 5),
)


class Review(models.Model):
    text = models.TextField(null=True, blank=True)
    stars = models.IntegerField(choices=CHOICES)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE,
                              related_name='movie_reviews')
