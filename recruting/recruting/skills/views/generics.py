from django.http import Http404
from django.shortcuts import get_object_or_404

from rest_framework import generics
from rest_framework.response import Response

from ..models import Position,Category
from ..serializers import CategorySerializer, PositionSerializer


class CategoryList(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    def get_queryset(self):
        return Category.objects.all()


class CategoryDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    def put(self, request, *args, **kwargs):
        try:
            if request.user.role == 1:
                return self.update(request, *args, **kwargs)
            else:
                return Response('Permission denied!!!')
        except Exception as e:
            return Response('Please Authorized!!!')

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        try:
            if request.user.role == 1:
                return self.destroy(request, *args, **kwargs)
            else:
                return Response('Permission denied!!!')
        except Exception as e:
            return Response('Please Authorized!!!')


class PositionList(generics.ListCreateAPIView):
    serializer_class = PositionSerializer

    def get_queryset(self):
        category = get_object_or_404(Category, id=self.kwargs[self.lookup_field])
        return Position.objects.filter(department=category,)

    def perform_create(self, serializer):
        try:
            category = Category.objects.get(id=self.kwargs['pk'])
        except Category.DoesNotExist:
            raise Http404
        serializer.save(department=category)
