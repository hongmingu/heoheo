from rest_framework import serializers
from blog.models import Post
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    related_postwriter = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'related_postwriter')


class PostSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')
    class Meta:
        model = Post
        fields = ('id', 'created_date', 'author', 'text', 'image')
    def create(self, validated_data):
        validated_data['author'] = self.context['request'].user
        return super(PostSerializer, self).create(validated_data)
