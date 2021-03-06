from rest_framework import permissions


class UpdateOwnProfile(permissions.BasePermission):
    """allow users to edit their own profile"""

    def has_object_permission(self, request, view, obj):
        """check users is trying to edit their own profile"""
        if request.method in permissions.SAFE_METHODS:
            return True

        return request.user.id == obj.id


class UpdateOwnStatus(permissions.BasePermission):
    """allow users to edit their own profile"""

    def has_object_permission(self, request, view, obj):
        """check users is trying edit their own status"""
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.user_profile.id == request.user.id