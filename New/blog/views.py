from django.shortcuts import render
from django.http import HttpResponse
from django.utils import timezone
from django.contrib.gis.geos import GEOSGeometry
from django.contrib.gis.measure import D
from datetime import datetime, timedelta
from blog.models import Post
from blog.serializers import PostSerializer, UserSerializer
from rest_framework import filters, viewsets, generics
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User


class PostViewSet(viewsets.ModelViewSet):
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]
    queryset = Post.objects.all()

    def get_queryset(self) :
        lat = self.request.GET.get('user_lat', '15')
        lon = self.request.GET.get('user_lon', '13')
        userpoint = GEOSGeometry('POINT(' + lon + ' ' + lat + ')', srid=4326)
        self.result = []
        i = 1
        while i<20:
            elasped_minutes = datetime.now() - timedelta(minutes=10*i)
            list_i = Post.objects.filter(created_date__gte = elasped_minutes).filter(point__distance_lte = (userpoint, D(m=i*500))).order_by("-created_date")
            [self.result.append(v) for v in list_i if v not in self.result]
            if len(self.result) > 50:
                self.result = self.result[:50]
                break
            i += 1
        return self.result

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
