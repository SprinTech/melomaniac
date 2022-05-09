from django.db import models
from backend.users.models import User

class Song(models.Model):
    class AudioFormat(models.TextChoices):
        Spotify = "Spotify"
        AudioFile = "AudioFile"
        Micro = "Micro"

    title = models.CharField(max_length=255, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    format = models.CharField(max_length=100, choices=AudioFormat.choices)
    users = models.ManyToManyField(User)

    def __str__(self) -> str:
        return self.title