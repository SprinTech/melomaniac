from rest_framework import viewsets, serializers
from .models import Song

class SongSerializer(serializers.ModelSerializer):
    created_at = serializers.DateTimeField(format="%d-%m-%Y %H:%M:%S", required=False)
    
    class Meta:
        model = Song
        fields = '__all__'