from rest_framework import serializers
from .models import TrackRating, Review

SCORE_CHOICES = [
    0.0, 0.5, 1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0, 4.5, 5.0
]


class TrackRatingSerializer(serializers.ModelSerializer):
    score = serializers.ChoiceField(choices=SCORE_CHOICES)
    
    class Meta:
        model = TrackRating
        fields = "__all__"


class ReviewSerializer(serializers.ModelSerializer):
    rating = serializers.ChoiceField(choices=SCORE_CHOICES)
    
    class Meta:
        model = Review
        fields = "__all__"

    