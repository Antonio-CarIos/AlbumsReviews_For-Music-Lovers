from django.db import models


class Track(models.Model):
    name = models.CharField(max_length=400)
    album = models.ForeignKey("Album", on_delete=models.CASCADE, related_name="tracks")

    def __str__(self):
        return f"{self.name} - {self.album.name_album}"
    


class Genres(models.Model):
    name_genres = models.CharField(max_length=100)

    def __str__(self):
        return self.name_genres


class Album(models.Model):
    name_album = models.CharField(max_length=250)
    album_cover = models.ImageField(upload_to="albums_covers", blank=True, null=True)
    favorite = models.BooleanField(default=False)
    artist = models.ForeignKey(
        "Artist", on_delete=models.CASCADE, related_name="albums"
    )
    genres = models.ManyToManyField(Genres)

    def __str__(self):
        return f"{self.name_album} - {self.artist.name_artist}"


class Artist(models.Model):
    name_artist = models.CharField(max_length=300)
    description = models.TextField()
    listeners = models.IntegerField()
    photo = models.ImageField(upload_to="artists", blank=True, null=True)

    def __str__(self):
        return self.name_artist
