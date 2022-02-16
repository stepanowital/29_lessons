from update_view.views import StoreUpdateView
from django.urls import path

urlpatterns = [
    path("update_view/<int:pk>/", StoreUpdateView.as_view())
]
