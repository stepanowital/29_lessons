from django.contrib import admin
from django.urls import include, path

# TODO здесь можно подключить urls Ваших приложений

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("router.urls")),
    path("", include("lookup_queries.urls")),
    path("", include("lookup_queries_2.urls")),
    path("", include("lookup_queries_3.urls")),
    path("", include("qf_queries.urls")),
    # path("", include("qf_queries_2.urls")),
    path("", include("fk_search.urls")),
    path("", include("delete_if_null.urls"))
]
