from django.shortcuts import render
from django.http import HttpResponse
from django.utils import timezone
from datetime import datetime, timedelta
from blog.models import Post
from blog.serializers import PostSerializer, UserSerializer
from rest_framework import filters, viewsets, generics
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated
from allauth.socialaccount.providers.facebook.views import FacebookOAuth2Adapter
from rest_auth.registration.views import SocialLoginView
from django.contrib.auth.models import User


class FacebookLogin(SocialLoginView):
    adapter_class = FacebookOAuth2Adapter


class PostViewSet(viewsets.ModelViewSet):
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]
    queryset = Post.objects.all()
    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
