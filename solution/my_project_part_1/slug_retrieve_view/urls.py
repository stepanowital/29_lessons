from slug_retrieve_view.views import StoreRetrieveView
from django.urls import path

urlpatterns = [
    path("slug_retrieve_view/<str:slug>/", StoreRetrieveView.as_view())
]
