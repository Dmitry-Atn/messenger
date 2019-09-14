from messenger.api.viewsets import MessagesViewSet, UsersViewSet
from rest_framework import routers

router = routers.DefaultRouter(trailing_slash=False)
router.register('messages', MessagesViewSet, basename='message')
router.register('users', UsersViewSet)
urlpatterns = router.urls

