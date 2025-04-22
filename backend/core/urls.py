from django.urls import path
from .views import ProfileListCreateAPIView, ProfileRetrieveUpdateDestroyAPIView

app_name = "core"

urlpatterns = [
    path("profiles/", ProfileListCreateAPIView.as_view(), name="profile-list"),
    path("profiles/<int:pk>/", ProfileRetrieveUpdateDestroyAPIView.as_view(), name="profile-detail"),
]
