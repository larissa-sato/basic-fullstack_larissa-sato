from rest_framework import serializers
from user.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password']
        extra_kwargs = {'password': {'write_only':True}}

        def create(self, validated_data: dict) -> User:
            client = User.objects.create_superuser(**validated_data)
            return client

        def update(self, instance: User, validated_data: dict) -> User:
            for key, value in validated_data.items():
                setattr(instance, key, value)

            instance.save()
            return instance