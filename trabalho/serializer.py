from rest_framework import serializers

from trabalho.models import Trabalho


class TrabalhoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trabalho
        fields = '__all__'
