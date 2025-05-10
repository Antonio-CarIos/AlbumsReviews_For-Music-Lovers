from django.contrib import admin
from .models import TrackRating, Review


class TrackRatingAdmin(admin.ModelAdmin):
    list_display = ("score",)
    search_fields = ("score",)


admin.site.register(TrackRating, TrackRatingAdmin)


class ReviewAdmin(admin.ModelAdmin):
    list_display = ("rating", "comment")


admin.site.register(Review, ReviewAdmin)
