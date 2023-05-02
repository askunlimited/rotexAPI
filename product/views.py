from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.permissions import (
    IsAuthenticated,
    AllowAny,
    IsAuthenticatedOrReadOnly,
)
from rest_framework import status, generics, mixins, viewsets
from rest_framework.decorators import api_view, APIView, permission_classes
from django.shortcuts import get_object_or_404

from .models import Category, Product
from .serializers import CategorySerializer, ProductSerializer
from .permissions import ReadOnly, AuthorOrReadOnly
from rest_framework.parsers import MultiPartParser, FormParser


class CategoryListCreateView(
    generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin
):
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Category.objects.all()

    def perform_create(self, serializer):
        user = self.request.user
        serializer.save()
        return super().perform_create(serializer)

    def get(self, request: Request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request: Request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class CategoryRetrieveUpdateDeleteView(
    generics.GenericAPIView,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
):
    serializer_class = CategorySerializer
    permission_classes = [AuthorOrReadOnly]
    queryset = Category.objects.all()

    def get(self, request: Request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request: Request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request: Request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


class ProductListCreateView(
    generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin
):
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Product.objects.all()
    parser_classes = (MultiPartParser, FormParser)

    def perform_create(self, serializer):
        user = self.request.user
        serializer.save(author=user)
        return super().perform_create(serializer)

    def get(self, request: Request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request: Request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class ProductRetrieveUpdateDeleteView(
    generics.GenericAPIView,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
):
    serializer_class = ProductSerializer
    permission_classes = [AuthorOrReadOnly]
    queryset = Product.objects.all()

    def get(self, request: Request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request: Request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request: Request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


class ListProductForAuthor(generics.GenericAPIView, mixins.ListModelMixin):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [AuthorOrReadOnly]

    def get_queryset(self):
        user = self.request.user
        return Product.objects.filter(author=user)

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class ListProductByCategory(generics.GenericAPIView, mixins.ListModelMixin):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [AuthorOrReadOnly]

    def get_queryset(self):
        category = self.request.category
        return Product.objects.filter(category=category)

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
