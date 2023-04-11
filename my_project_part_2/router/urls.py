# TODO опишите здесь маршрутизацию с помощью класса SimpleRouter
from rest_framework import routers

from router.views import StoreViewSet

router = routers.SimpleRouter()
router.register('router_stores', StoreViewSet)

urlpatterns = [

]

urlpatterns += router.urls
