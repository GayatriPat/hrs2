from rest_framework import serializers
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=65, min_length=8, write_only=True)
    email = serializers.EmailField(max_length=255, min_length=2)

    class Meta:
        model = User
        fields = (
            'username',
            'email',
            'password'
        )

    def validate(self, attrs):
        print(attrs)
        email = attrs.get('email', '')
        if User.objects.filter(email=email).exists():
            raise serializers.ValidationError({'email': ('Email is already in use')})
        return super().validate(attrs)

    def create(self, validated_data):
        print("validate data", validated_data)
        username = validated_data.get('username')
        password = validated_data.get('password')
        email = validated_data.get('email')
        return User.objects.create_user(username=username, password=password, email=email)
