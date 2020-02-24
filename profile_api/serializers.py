from rest_framework import serializers


class HelloApiSerializer(serializers.Serializer):
    """serializes a name field to test API"""
    name = serializers.CharField(max_length=10)