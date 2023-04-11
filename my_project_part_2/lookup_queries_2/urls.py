# TODO здесь необходимо настроить urls приложения
from rest_framework import routers

from lookup_queries_2.views import StoreView

router = routers.SimpleRouter()
router.register('lookup_queries_2', StoreView)

urlpatterns = [

]

urlpatterns += router.urls
