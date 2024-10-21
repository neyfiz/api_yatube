"""Сериализаторы для приложения posts."""

from rest_framework import serializers

from posts.models import Post, Group, Comment


class PostSerializer(serializers.ModelSerializer):
    """Сериализатор для модели Post."""

    author = serializers.CharField(source='author.username', read_only=True)

    class Meta:
        """Мета-информация для сериализатора Post."""

        model = Post
        fields = '__all__'


class GroupSerializer(serializers.ModelSerializer):
    """Сериализатор для модели Group."""

    class Meta:
        """Мета-информация для сериализатора Group."""

        model = Group
        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):
    """Сериализатор для модели Comment."""

    author = serializers.CharField(source='author.username', read_only=True)
    post = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        """Мета-информация для сериализатора Comment."""

        model = Comment
        fields = '__all__'
