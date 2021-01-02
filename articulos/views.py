from django.shortcuts import render
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.views.generic import View
from .models import Articulo



class ArticulosListView(PermissionRequiredMixin, View):

    permission_required = ('articulos.view_articulo')

    def get(self, request):
        articulos_objects = Articulo.objects.all()
        context = {"articulos_objects": articulos_objects}
        return render(request, 'articulos/list.html', context)
