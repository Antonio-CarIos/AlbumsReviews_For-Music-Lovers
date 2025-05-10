from django.contrib import admin
from .models import Track, Genres, Album, Artist


class TrackAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)


admin.site.register(Track, TrackAdmin)


class GenresAdmin(admin.ModelAdmin):
    list_display = ("name_genres",)
    search_fields = ("name_genres",)


admin.site.register(Genres, GenresAdmin)


class AlbumAdmin(admin.ModelAdmin):
    list_display = ("name_album", "album_cover", "favorite")
    search_fields = ("name_album",)


admin.site.register(Album, AlbumAdmin)


class ArtistAdmin(admin.ModelAdmin):
    list_display = ("name_artist", "description", "listeners", "photo")
    search_fields = ("name_artist",)


admin.site.register(Artist, ArtistAdmin)
