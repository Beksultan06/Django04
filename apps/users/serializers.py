from rest_framework import serializers
from apps.users.models import GeekUser

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = GeekUser
        fields = "__all__"
        
class UserDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = GeekUser
        fields = "__all__"