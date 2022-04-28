from django.db import models

class SubmitionType:
    spotify = "Spotify"
    audio_file = "Audio File"
    micro = "Micro"

class Song(models.Model):
    class SubmitionType(models.TextChoices):
        spotify = "Spotify"
        audio_file = "Audio File"
        micro = "Micro"

    title = models.CharField(max_length=255, null=False)
    submission_type = models.CharField(max_length=100, choices=SubmitionType.choices)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title

class User(models.Model):
    username = models.CharField(max_length=50, null=False, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    email = models.EmailField(max_length=254, null=False, unique=True)
    password = models.CharField(max_length=254, null=False, unique=True)
    
    def __str__(self):
        return self.username