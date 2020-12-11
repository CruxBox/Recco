from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token
from rest_framework import serializers

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):

    favourite = serializers.ReadOnlyField(source='get_favourite_watchlist_id')
    seen = serializers.ReadOnlyField(source='get_seen_watchlist_id')
    class Meta:
        model = User
        fields = ('id', 'username', 'email','contribution','favourite','seen')


class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(
            validated_data['username'], validated_data['email'], validated_data['password'])
        return user
