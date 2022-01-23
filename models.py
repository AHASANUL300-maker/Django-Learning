from django.db import models
from django.contrib.auth.models import User



""" Details of the Film """


class Film(models.Model):
    title = models.CharField(max_length=250)
    media = models.ForeignKey(Media, on_delete=models.CASCADE)
    film_rate_comment = models.ForeignKey(FilmRatingComment, on_delete=models.CASCADE)
    cast = models.ForeignKey(Cast, on_delete=models.CASCADE)


""" Details about the Cast of the film"""


class Cast(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    film = models.ForeignKey(Film, on_delete=models.CASCADE)
    profession = models.ForeignKey(Profession, on_delete=models.CASCADE)
    film_characer_name = models.CharField(max_length=70)


""" Film Rating & Comments """


class FilmRatingComment(models.Model):
    film = models.ForeignKey(Film, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.PositiveIntegerField()
    comment = models.TextField(max_length=1000)


""" Media """


class Media(models.Model):
    film = models.ForeignKey(Film, on_delete=models.CASCADE)
    image = models.ImageField(upload_to=None)
    video = models.FileField(upload_to=None)


""" Genre Name """


class Genre(models.Model):
    name = models.CharField(max_length=70)


"""  Film Genre """


class FilmGenre(models.Model):
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    film = models.ForeignKey(Film, on_delete=models.CASCADE)


class Profession(models.Model):
    name = models.CharField(max_length=70)

