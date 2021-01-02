from django.urls import path
from .views import ArticulosListView

urlpatterns = [
    path('list/', ArticulosListView.as_view())
]
