from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from profile_api import serializers

class HelloApiVew(APIView):
    """TEST API VIEW"""
    serializer_class = serializers.HelloApiSerializer

    def get(self, request, format=None):
        """return a list of content"""
        an_apiview = [
            'The authentication that comes with Django is good enough for most common cases,',
            'but you may have needs not met by the out-of-the-box defaults.',
            'To customize authentication to your projects needs involves understanding what points of the provided system are extensible or replaceable.',
            ' This document provides details about how the auth system can be customized.',
        ]

        return Response({"message":"hello", "an_apiview": an_apiview})

    def post(self, request):
        """post a msg"""
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            msg = f'hello {name}'
            return Response({'massage': msg})
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )

    def put(self, request, pk=None):
        """updating an object"""
        return Response({'method': 'PUT'})

    def patch(self, request, pk=None):
        """partial update of object"""
        return Response({'method': 'PATCH'})

    def delete(self, request, pk=None):
        """delete an object"""
        return Response({'method': 'DELETE'})