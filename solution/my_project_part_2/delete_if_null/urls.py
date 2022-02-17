from django.urls import path

from delete_if_null import views


urlpatterns = [
   path('delete_if_null/', views.StoreListView.as_view())
]
