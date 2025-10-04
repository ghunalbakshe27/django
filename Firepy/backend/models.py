from django.contrib.auth.models import AbstractUser
from django.db import models

class customuser(AbstractUser):
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=30)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', 'first_name']

    def __str__(self):
        return self.username

# Define your models here
class Music(models.Model):
    title = models.CharField(max_length=200)
    artist = models.CharField(max_length=100)
    genre = models.CharField(max_length=100)
    release_date = models.DateField()
    duration = models.DurationField()
    album = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return f"{self.title} by {self.artist}"

class Genre(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class User(models.Model):
    username = models.CharField(max_length=150, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)

    def __str__(self):
        return self.username

class Playlist(models.Model):
    name = models.CharField(max_length=200)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    songs = models.ManyToManyField(Music)

    def __str__(self):
        return self.name