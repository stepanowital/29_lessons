# TODO здесь необходимо настроить urls приложения
from rest_framework import routers

from lookup_queries.views import StoreView

router = routers.SimpleRouter()
router.register('lookup_queries', StoreView)

urlpatterns = [

]

urlpatterns += router.urls
