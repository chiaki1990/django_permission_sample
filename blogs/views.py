from django.shortcuts import render
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.views.generic import View
from .models import Blog



class BlogListView(PermissionRequiredMixin, View):

    permission_required = ('blogs.view_blog')

    def get(self, request):
        blog_objects = Blog.objects.all()
        context = {"blog_objects": blog_objects}
        return render(request, 'blogs/list.html', context)
