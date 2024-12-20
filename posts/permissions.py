from rest_framework import permissions

class IsAuthorOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        #authenticated users can only see list view
        if request.user.is_authenticated:
            return True
        return False

    def has_object_permission(self, request, view, obj):
        #read permissions are allowed to any request
        if request.method in permissions.SAFE_METHODS:
            return True
        #write permissions are only allowed to the owner of the post
        return obj.author == request.user