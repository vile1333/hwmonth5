from django.db import models


# Create your models here.

class Director(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    @property
    def movies_count(self):
        return self.directed_movies.count()

class Movie(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    duration = models.DurationField()
    director = models.ForeignKey(Director,related_name='directed_movies', on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class Review(models.Model):
    movie = models.ForeignKey(Movie, related_name="reviews", on_delete=models.CASCADE)
    text = models.TextField()
    stars = models.IntegerField(choices=[(i, i) for i in range(1, 6)],default=3)  # рейтинг от 1 до 5

    def __str__(self):
        return f"Review for {self.movie.title} - {self.stars} stars"
