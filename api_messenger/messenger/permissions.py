from rest_framework import permissions


class MessagePermission(permissions.BasePermission):
    message = 'You are not allowed to view this message'

    def has_object_permission(self, request, view, obj):
        return obj.sender == request.user or obj.recipient == request.user


class MessageOwnerPermission(MessagePermission):
    message = 'Insufficient permission'

    def has_object_permission(self, request, view, obj):
        return obj.sender == request.user