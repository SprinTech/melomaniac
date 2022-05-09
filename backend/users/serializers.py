from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    created_at = serializers.DateTimeField(format="%d-%m-%Y %H:%M:%S", required=False)
    updated_at = serializers.DateTimeField(format="%d-%m-%Y %H:%M:%S", required=False)
    
    class Meta:
        model = User
        fields = '__all__'