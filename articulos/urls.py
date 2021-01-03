from django.urls import path
from .views import ArticulosListView

urlpatterns = [
    path('', ArticulosListView.as_view())
]
