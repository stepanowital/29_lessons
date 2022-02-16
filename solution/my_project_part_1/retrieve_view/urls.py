from retrieve_view.views import StoreRetrieveView
from django.urls import path

urlpatterns = [path("retrieve_view/<int:pk>/", StoreRetrieveView.as_view())]
