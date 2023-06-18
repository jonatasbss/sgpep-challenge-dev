from rest_framework import serializers
from .models import Proposta
from apps.usuario.models import CustomUser


class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('email',)


class PropostaSerializer(serializers.ModelSerializer):
    cliente = CustomUserSerializer()

    class Meta:
        model = Proposta
        fields = '__all__'

    def create(self, validated_data):
        cliente_data = validated_data.pop('cliente')
        cliente = CustomUser.objects.create(**cliente_data)
        validated_data['cliente'] = cliente
        return super().create(validated_data)
