from django.db import models
from django.contrib.auth.models import AbstractUser, User
from django import forms

# Create your models here.

class Film(models. Model):
    title = models.CharField(max_length=100)
    media = models.ForeignKey(Media, on_delete=models.CASCADE)
    film_rate_comment = models.ForeignKey(FilmRatingComment, on_delete=models.CASCADE)
    crew = models.ForeignKey(Crew, on_delete=models.CASCADE)


class FilmRatingComment(models.Model):
    film = models.ForeignKey(Film, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField()
    comment = models.TextField()


class Crew(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    film = models.ForeignKey(Film, on_delete=models.CASCADE)
    profession = models.ForeignKey(Profession, on_delete=models.CASCADE)
    film_Char_Name = models.CharField(max_length= 100)


class FilmGenre(models.Model):
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    film = models.ForeignKey(Film, on_delete=models.CASCADE)


class Profession(forms.Form):
    role = ('Actor', 'Actress', 'Director', 'Producer', 'Writer', 'Editor')
    prof = forms.ChoiceField(choices= role)


class Genre(forms.Form):
    name = ('Action', 'Thriller', 'Romance', 'Horror', 'Fantasy', 'Crime')
    genre = forms.ChoiceField(choices= name)


class Media(models. Model):
    videos = models.FileField(upload_to='videos uploaded', null=True)
    image = models.ImageField(upload_to='image uploaded', null=True)
    film = models.ForeignKey(Film, on_delete=models.CASCADE, )


class Profile(AbstractUser):
    user_name = models.CharField(max_length= 50)
    user_email = models.EmailField(max_length=100)
    user_password = models.CharField(max_length=250)
    birth_date = models.DateField(null=True, blank=True)
    sex = models.CharField(max_length=20)


















