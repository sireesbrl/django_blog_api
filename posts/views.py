from django.shortcuts import render
from rest_framework import viewsets, permissions
from .serializers import PostSerializer, UserSerializer
from .models import Post
from .permissions import IsAuthorOrReadOnly
from django.contrib.auth import get_user_model


class PostViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthorOrReadOnly]
    serializer_class = PostSerializer
    queryset = Post.objects.all()

class UserViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAdminUser]
    serializer_class = UserSerializer
    queryset = get_user_model().objects.all()