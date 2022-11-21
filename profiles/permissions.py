from rest_framework import permissions


class UpdateOwnProfile(permissions.BasePermission):
    '''allow users to make changes only to their profiles'''

    def has_object_permission(self, request, view, obj):
        print(request.user, obj.id, request.headers.get('Authorization'))
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.id == request.user.id
