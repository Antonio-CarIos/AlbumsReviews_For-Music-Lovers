from django.db import models
from django.contrib.auth.models import AbstractUser


class Profile(AbstractUser):
    description = models.TextField()
    profile_picture = models.ImageField(upload_to="profiles/", blank=True, null=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    fav_genres = models.ManyToManyField("music.Genres", blank=True)
    fav_artist = models.ManyToManyField("music.Artist", blank=True)
    fav_albums = models.ManyToManyField("music.Album", blank=True)

    def __str__(self):
        return self.username
