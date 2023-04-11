from list_view.views import StoreListView
from django.urls import path

urlpatterns = [
    path("list_view/", StoreListView.as_view())
]
