from rest_framework import serializers
from bolg.models import Post
from django.contrib.auth.models import User
from drf_extra_fields.geo_fields import PointField


class UserSerializer(serializers.ModelSerializer):
    related_postwriter = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'related_postwriter')


class PostSerializer(serializers.ModelSerializer):
    point = PointField(required=True)
    class Meta:
        model = Post
        fields = ('id', 'created_date', 'author', 'text', 'point', 'image')
    def create(self, validated_data):
        validated_data['author'] = self.context['request'].user
        return super(PostSerializer, self).create(validated_data)
