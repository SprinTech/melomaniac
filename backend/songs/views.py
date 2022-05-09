from .serializers import SongSerializer
from .models import Song
from rest_framework.generics import RetrieveAPIView, ListAPIView, CreateAPIView

class SongDetail(RetrieveAPIView):
    queryset = Song.objects.all()
    serializer_class = SongSerializer

class SongList(ListAPIView):
    queryset = Song.objects.all()
    serializer_class = SongSerializer

class SongCreate(CreateAPIView):
    queryset = Song.objects.all()
    serializer_class = SongSerializer