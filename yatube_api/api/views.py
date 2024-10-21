"""Модуль для реализации ViewSet-ов API приложения posts."""

from rest_framework import viewsets
from rest_framework.exceptions import PermissionDenied
from django.shortcuts import get_object_or_404

from .serializers import PostSerializer, GroupSerializer, CommentSerializer
from posts.models import Post, Group, Comment


class PostViewSet(viewsets.ModelViewSet):
    """ViewSet для работы с постами."""

    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def perform_create(self, serializer):
        """Создание нового поста, привязанного к текущему пользователю."""
        serializer.save(author=self.request.user)

    def perform_update(self, serializer):
        """Обновление поста разрешенно только автору."""
        if serializer.instance.author != self.request.user:
            raise PermissionDenied('Изменение чужого контента запрещено!')
        super(PostViewSet, self).perform_update(serializer)

    def perform_destroy(self, instance):
        """Удаление поста разрешенно только автору."""
        if instance.author != self.request.user:
            raise PermissionDenied('Удаление чужого контента запрещено!')
        instance.delete()


class CommentViewSet(viewsets.ModelViewSet):
    """ViewSet для работы с комментариями."""

    serializer_class = CommentSerializer

    def get_queryset(self):
        """Получение комментариев, связанных с конкретным постом."""
        post_id = self.kwargs.get('post_id')
        return Comment.objects.filter(post__id=post_id)

    def perform_create(self, serializer):
        """Создание комментария привязанно к пользователю и посту."""
        post = get_object_or_404(Post, id=self.kwargs.get('post_id'))
        serializer.save(author=self.request.user, post=post)

    def perform_update(self, serializer):
        """Обновление комментария разрешенно только автору."""
        if serializer.instance.author != self.request.user:
            raise PermissionDenied('Изменение чужого комментария запрещено!')
        super(CommentViewSet, self).perform_update(serializer)

    def perform_destroy(self, instance):
        """Удаление комментария разрешенно только автору."""
        if instance.author != self.request.user:
            raise PermissionDenied('Удаление чужого комментария запрещено!')
        instance.delete()


class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    """ViewSet для работы с группами."""

    queryset = Group.objects.all()
    serializer_class = GroupSerializer
