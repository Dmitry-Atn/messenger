from rest_framework import generics, viewsets, status
from messenger.models import Message, create_message
from messenger.permissions import MessagePermission, MessageOwnerPermission
from .serializers import MessagesSerializer, UserSerializer
from django.contrib.auth.models import User
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from django.db.models import Q
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect


class MessagesViewSet(viewsets.ModelViewSet):
    serializer_class = MessagesSerializer

    def get_queryset(self):
        return Message.objects.all()

    def get_permissions(self):
        return [MessagePermission()]

    def create(self, request, *args, **kwargs):
        create_message(request.user, User.objects.get(pk=request.POST.get("recipient")), request.POST.get("body"))
        return HttpResponseRedirect('/api/messages')

    def list(self, request):
        queryset = Message.objects.filter((Q(sender=request.user) | Q(recipient=request.user)) & Q(deleted=False))
        permission_classes = [MessagePermission]
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        permission_classes = [MessagePermission]
        queryset = Message.objects.filter((Q(sender=request.user) | Q(recipient=request.user)) & Q(deleted=False))
        queryset.filter(pk=pk).update(read=True)
        message = get_object_or_404(queryset, pk=pk)
        serializer = self.get_serializer(message)
        return Response(serializer.data)

    def destroy(self, request, pk=None, *args, **kwargs):
        if MessageOwnerPermission().has_object_permission(request, None, Message.objects.get(pk=pk)):
            if Message.objects.get(pk=pk).deleted:
                return Response({"detail":"Not found."}, status=status.HTTP_404_NOT_FOUND)
            Message.objects.filter(pk=pk).update(deleted=True)
            return HttpResponseRedirect('/api/messages')
        return Response({"detail":"Not permitted."}, status=status.HTTP_403_FORBIDDEN)


class UsersViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = User.objects.all()
    serializer_class = UserSerializer



