from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

class TrackRating(models.Model):
    score = models.DecimalField(
        max_digits=2,
        decimal_places=1, 
        validators=[MinValueValidator(0.0), MaxValueValidator(5.0)]
    )
    track = models.ForeignKey(
        "music.Track", on_delete=models.CASCADE, related_name="rating"
    )
    user = models.ForeignKey(
        "core.Profile", on_delete=models.CASCADE, related_name="track_rating"
    )

    def __str__(self):
        return f"{self.user.username} {self.track.name} - {self.score}"


class Review(models.Model):
    rating = models.DecimalField(
        max_digits=2,
        decimal_places=1,
        validators=[MinValueValidator(0.0), MaxValueValidator(5.0)]
    )
    comment = models.TextField()
    user = models.ForeignKey(
        "core.Profile", on_delete=models.CASCADE, related_name="reviews"
    )
    album = models.ForeignKey(
        "music.Album", on_delete=models.CASCADE, related_name="reviews"
    )

    def __str__(self):
        return f"{self.user.username} {self.album.name_album} - {self.rating}"
