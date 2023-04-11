# TODO здесь необходимо настроить urls приложения
from rest_framework import routers

from delete_if_null.views import StoreView

router = routers.SimpleRouter()
router.register('delete_if_null', StoreView)

urlpatterns = [

]

urlpatterns += router.urls
