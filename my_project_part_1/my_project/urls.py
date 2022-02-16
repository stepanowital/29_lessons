from django.contrib import admin
from django.urls import include, path

# TODO здесь можно подключить urls Ваших приложений

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("list_view.urls")),
    path("", include("retrieve_view.urls")),
    path("", include("slug_retrieve_view.urls")),
    path("", include("update_view.urls")),
    path("", include("simple_serializer.urls")),
    path("", include("fk_serializer.urls")),
    path("", include("m2m_serializer.urls")),
    # path("", include(" .urls")),
]
