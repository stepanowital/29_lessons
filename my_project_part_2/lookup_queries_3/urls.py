# TODO здесь необходимо настроить urls приложения
from rest_framework import routers

from lookup_queries_3.views import StoreView

router = routers.SimpleRouter()
router.register('lookup_queries_3', StoreView)

urlpatterns = [

]

urlpatterns += router.urls
