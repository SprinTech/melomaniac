from .serializers import UserSerializer
from .models import User
from rest_framework.generics import RetrieveAPIView, ListAPIView, CreateAPIView, DestroyAPIView, UpdateAPIView

class UserDetail(RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserList(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserCreate(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDelete(DestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserUpdate(UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer