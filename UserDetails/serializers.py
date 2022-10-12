from rest_framework import serializers
from .models import UserData
from UserDetails import models


class UserDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.UserData
        fields = '__all__'