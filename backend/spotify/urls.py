from django.urls import path
from .views import AuthURL, spotify_callback, IsAuthenticated

urlpatterns = [
    path('login', AuthURL.as_view()),
    path('callback', spotify_callback),
    path('is-authenticated', IsAuthenticated.as_view()),
]