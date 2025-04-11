from django.db import models
from django.contrib.auth.models import AbstractUser

class Perfil(AbstractUser):
    nickname = models.CharField(max_length=200)
    description = models.TextField()
    date_sign = models.DateTimeField(auto_now_add=True)
    fav_genres = models.ManyToManyField("music.Genres")
    fav_artist = models.ManyToManyField("music.Artist")
    fav_albums = models.ManyToManyField("music.Album")

    def __str__(self):
        return self.nickname


