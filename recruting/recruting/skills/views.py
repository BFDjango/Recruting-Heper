from django.shortcuts import render
from rest_framework import mixins, generics

from recruting.skills.models import Category
from recruting.skills.serializers import CategorySerializer


class DepartmentListAPIView(mixins.ListModelMixin,
                            mixins.CreateModelMixin,
                            generics.GenericAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


