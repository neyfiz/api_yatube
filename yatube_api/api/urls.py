"""URL-маршруты для API приложения posts."""

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token

from .views import PostViewSet, GroupViewSet, CommentViewSet

router = DefaultRouter()

router.register('posts', PostViewSet)
router.register('groups', GroupViewSet)
router.register(
    r'posts/(?P<post_id>\d+)/comments',
    CommentViewSet,
    basename='post-comments'
)

urlpatterns = [
    path('api/v1/api-token-auth/', obtain_auth_token),
    path('api/v1/', include(router.urls)),
]
