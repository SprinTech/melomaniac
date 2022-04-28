from rest_framework import viewsets, serializers
from .models import User, Song

class UserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = User
        fields = '__all__'

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class SongSerializer(serializers.ModelSerializer):

    class Meta:
        model = Song
        fields = '__all__'
    
class SongViewSet(viewsets.ModelViewSet):
    queryset = Song.objects.all()
    serializer_class = SongSerializer