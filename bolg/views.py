from django.shortcuts import render
from django.contrib.gis.geos import GEOSGeometry
from django.contrib.gis.measure import D
from django.http import HttpResponse
from django.utils import timezone
from datetime import datetime, timedelta
from bolg.models import Post
from bolg.serializers import PostSerializer, UserSerializer
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

    def get_queryset(self) :
        lon = self.request.GET.get('user_lon', '13')
        lat = self.request.GET.get('user_lat', '15')
        userpoint = GEOSGeometry('POINT(' + lon + ' ' + lat + ')', srid=4326)
        self.result = []
        i = 1
        while i<20:
            elasped_minutes = datetime.now() - timedelta(minutes=10*i)
            list_i = Post.objects.filter(created_date__gte = elasped_minutes).filter(point__distance_lte = (userpoint, D(km=i)))
            [self.result.append(v) for v in list_i if v not in self.result]
            if len(self.result) > 10:
                self.result = self.result[:8]
                break
            i += 1
        return self.result
