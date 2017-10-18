from django.core.serializers import serialize
from rest_framework import serializers
from main.models import *


class StreetSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=100)

    def create(self, validated_data):
        pass

    def update(self, instance, validated_data):
        return instance


class XstreetSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        print(validated_data)

    class Meta:
        model = Street
        fields = ('id', 'name')


class XdomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dom
        fields = ('id', 'name', 'num', 'buk', 'dom_street')
        