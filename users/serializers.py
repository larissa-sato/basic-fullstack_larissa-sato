from rest_framework import serializers
from users.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password']
        read_only_fields = ['is_superuser']
        extra_kwargs = {'password': {'write_only':True}}

        def create(self, validated_data: dict) -> User:
            client = User.objects.create_superuser(**validated_data)
            return client

        def update(self, instance: User, validated_data: dict) -> User:
            for key, value in validated_data.items():
                setattr(instance, key, value)

            instance.save()
            return instance