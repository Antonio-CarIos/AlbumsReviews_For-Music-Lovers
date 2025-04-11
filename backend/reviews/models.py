from django.db import models

class ScoreOptions(models.IntegerChoices):
    ZERO = 0, '0'
    UM = 1, '1'
    DOIS = 2, '2'
    TRES = 3, '3'
    QUATRO = 4, '4'
    CINCO = 5, '5'
    SEIS = 6, '6'
    SETE = 7, '7'
    OITO = 8, '8'
    NOVE = 9, '9'
    DEZ = 10, 10


class TrackRating(models.Model):
    score = models.IntegerField(choices=ScoreOptions.choices)
    track = models.ForeignKey("music.Track", on_delete=models.CASCADE, related_name='rating')
    user = models.ForeignKey("core.Perfil", on_delete=models.CASCADE, related_name='track_rating')

    def __str__(self):
        return f"{self.user.nickname} {self.track.name} - {self.score}"

class Review(models.Model):
    rating = models.IntegerField()
    comment = models.TextField()
    user = models.ForeignKey("core.Perfil", on_delete=models.CASCADE, related_name='reviews')
    album = models.ForeignKey("music.Album", on_delete=models.CASCADE, related_name='reviews')

    def __str__(self):
        return f"{self.user.nickname} {self.album.name_album}"