from django.urls import path
from . import views

urlpatterns = [
    path("", views.SongList.as_view(), name="song-list"),
    path("<int:pk>/", views.SongDetail.as_view(), name='song-detail'),
    path("create/", views.SongCreate.as_view(), name='song-create'),
]
