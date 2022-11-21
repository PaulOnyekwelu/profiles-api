from rest_framework import permissions


class UpdateOwnProfile(permissions.BasePermission):
    '''allow users to make changes only to their profiles'''

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.id == request.user.id


class UpdateOwnFeeds(permissions.BasePermission):
    '''allow user to update own feeds'''

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.user_profile.id == request.user.id
