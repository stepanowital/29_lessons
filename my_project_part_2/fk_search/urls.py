# TODO здесь необходимо настроить urls приложения
from rest_framework import routers

from fk_search.views import StoreView

router = routers.SimpleRouter()
router.register('fk_search', StoreView)

urlpatterns = [

]

urlpatterns += router.urls

