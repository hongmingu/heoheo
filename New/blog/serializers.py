from rest_framework import serializers
from blog.models import Post
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    related_postwriter = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    class Meta:
        model = User
        fields = ('username', 'email', 'related_postwriter')


class PostSerializer(serializers.HyperlinkedModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')
    image = serializers.HyperlinkedRelatedField(many=True, read_only=True)
    class Meta:
        model = Post
        fields = ('author', 'text', 'image')
    def create(self, validated_data):
        validated_data['author'] = self.context['request'].user
        return super(PostSerializer, self).create(validated_data)
