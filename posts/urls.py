from rest_framework.routers import SimpleRouter

from posts.views import UserViewSet, PostViewSet

router = SimpleRouter()

router.register(
    prefix='users',
    viewset=UserViewSet,
    basename='users'
)

router.register(
    prefix='',
    viewset=PostViewSet,
    basename='posts'
)

urlpatterns = router.urls
