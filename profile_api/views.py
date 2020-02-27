from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework import filters
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings
from rest_framework.permissions import IsAuthenticated

from profile_api import serializers
from profile_api import models
from profile_api import permissions

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


class HelloApiViewset(viewsets.ViewSet):
    """api viewset"""

    serializer_class = serializers.HelloApiSerializer
    def list(self, request):
        """return a message"""
        vs = [
            'actions include list, retrieve, destroy, update, partial update, create',
            'maps urls with router',
            'same functionality less code'
        ]
        return Response({"message": "hello viewset", 'aviewset': vs})

    def create(self, request):
        """create hello message"""
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            msg = f'hello...{name}'
            return Response({'message': msg})
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )

    def retrieve(self, request, pk=None):
        """Handle getting an object by its ID"""

        return Response({'http_method': 'GET'})

    def update(self, request, pk=None):
        """Handle updating an object"""

        return Response({'http_method': 'PUT'})

    def partial_update(self, request, pk=None):
        """Handle updating part of an object"""

        return Response({'http_method': 'PATCH'})

    def destroy(self, request, pk=None):
        """Handle removing an object"""

        return Response({'http_method': 'DELETE'})


class UserProfileViewSet(viewsets.ModelViewSet):
    """handling update and create user profile"""
    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
    authentication_classes = (TokenAuthentication, )
    permission_classes = (permissions.UpdateOwnProfile, )
    filter_backends = (filters.SearchFilter, )
    search_fields = ('name', 'email')


class UserLoginApiView(ObtainAuthToken):
    """creating user login tokens"""
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES

class ProfileFeedItemViewSet(viewsets.ModelViewSet):
    """handling user profile item update create del"""
    serializer_class = serializers.ProfileFeedItemSerializer
    authentication_classes = (TokenAuthentication, )
    queryset = models.ProfileFeedItem.objects.all()
    permission_classes = (permissions.UpdateOwnStatus, IsAuthenticated)

    def perform_create(self, serializer):
        """set the user profile to the logged in user"""
        serializer.save(user_profile=self.request.user)