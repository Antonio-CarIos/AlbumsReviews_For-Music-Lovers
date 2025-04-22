from rest_framework import serializers
from .models import Profile


class ProfileSerializer(serializers.ModelSerializer):
    profile_picture = serializers.ImageField(required=False)

    class Meta:
        model = Profile
        fields = [
            "id",
            "username",
            "email",
            "description",
            "profile_picture",
            "fav_genres",
            "fav_artist",
            "fav_albums",
            "date_joined",
            "password",
            
        ]

        read_only_fields = [
            "id",
            "date_joined",
        ]
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        fav_genres_data = validated_data.pop("fav_genres", [])
        fav_artist_data = validated_data.pop("fav_artist", [])
        fav_albums_data = validated_data.pop("fav_albums", [])

        password = validated_data.pop('password')
        user = Profile(**validated_data)
        user.set_password(password)
        user.save()
        user.fav_genres.set(fav_genres_data)
        user.fav_artist.set(fav_artist_data)
        user.fav_albums.set(fav_albums_data)
        return user
    
    def update(self, instance, validated_data):
        validated_data.pop('email', None) 
        return super().update(instance, validated_data)