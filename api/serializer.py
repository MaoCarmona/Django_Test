from rest_framework import serializers
from .models import *

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        # fields = ('name','age','created_at')
        fields = '__all__'