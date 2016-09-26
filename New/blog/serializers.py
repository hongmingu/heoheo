from rest_framework import serializers
from blog.models import Post
from django.contrib.auth.models import User
from drf_extra_fields.geo_fields import PointField


class UserSerializer(serializers.ModelSerializer):
    related_postwriter = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    class Meta:
        model = User
        fields = ('username', 'email', 'related_postwriter')


class PostSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')
    point = PointField(required=True) #이게 있는게 편한가 없는게 편한가 니가 결정
    class Meta:
        model = Post
        # fields = ('author', 'text', 'image', )
        fields = ('author', 'text', 'image', 'point', 'created_date')
    def create(self, validated_data):
        validated_data['author'] = self.context['request'].user
        return super(PostSerializer, self).create(validated_data)
