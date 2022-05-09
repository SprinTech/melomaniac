import os
from django.shortcuts import redirect
from rest_framework.views import APIView
from requests import Request, post
from rest_framework import status
from rest_framework.response import Response
from .utils import create_or_update_user_tokens, is_spotify_authenticated

from dotenv import load_dotenv
load_dotenv()

REDIRECT_URI=os.getenv("REDIRECT_URI")
CLIENT_ID=os.getenv("CLIENT_ID")
CLIENT_SECRET=os.getenv("CLIENT_SECRET")

class AuthURL(APIView):
    def get(self, request, format=None):
        scopes = 'playlist-read-private user-read-private user-read-email'

        url = Request('GET', 'https://accounts.spotify.com/authorize', params={
            'scopes': scopes,
            'response_type': 'code',
            'redirect_uri': REDIRECT_URI,
            'client_id': CLIENT_ID
        }).prepare().url
        res = Response({'url': url}, status=status.HTTP_200_OK)
        return res
    
def spotify_callback(request, format=None):
    code = request.GET.get('code')
    error = request.GET.get('error')

    response = post("https://accounts.spotify.com/api/token", data={
        'grant_type': 'authorization_code',
        'code': code,
        'redirect_uri': REDIRECT_URI,
        'client_id': CLIENT_ID,
        'client_secret': CLIENT_SECRET
    }).json()

    access_token = response.get('access_token')
    token_type = response.get('token_type')
    refresh_token = response.get('refresh_token')
    expires_in = response.get('expires_in')
    error = response.get('error')

    if not request.session.exists(request.session.session_key):
        request.session.create()

    create_or_update_user_tokens(request.session.session_key, access_token, refresh_token, token_type, expires_in)
    return redirect('/api/users/')

class IsAuthenticated(APIView):
    def get(self, request, format=None):
        is_authenticated = is_spotify_authenticated(self.request.session.session_key)
        return Response({'status': is_authenticated}, status=status.HTTP_200_OK)