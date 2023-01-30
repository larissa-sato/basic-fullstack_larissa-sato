from rest_framework import serializers
from clients.models import Client


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = [
            "name",
            "email",
            "telefone",
        ]

        extra_kwargs = {
            "created_at": {"read_only": True},
        }

        def create(self, validated_data: dict) -> Client:
            client = Client.objects.create_user(**validated_data)
            return client

