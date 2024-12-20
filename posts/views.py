from django.shortcuts import render
from rest_framework import generics, permissions
from .serializers import PostSerializer
from .models import Post
from .permissions import IsAuthorOrReadOnly


class PostList(generics.ListCreateAPIView):
    permission_classes = [IsAuthorOrReadOnly,]
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    ermission_classes = [IsAuthorOrReadOnly,]
    queryset = Post.objects.all()
    serializer_class = PostSerializer