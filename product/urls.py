from django.urls import path
from .views import (
    CategoryListCreateView,
    CategoryRetrieveUpdateDeleteView,
    ProductListCreateView,
    ProductRetrieveUpdateDeleteView,
)

urlpatterns = [
    path("", ProductListCreateView.as_view(), name="list_product"),
    path("category/", CategoryListCreateView.as_view(), name="list_category"),
    path(
        "category/<int:pk>/",
        CategoryRetrieveUpdateDeleteView.as_view(),
        name="category_detail",
    ),
    path(
        "<int:pk>/",
        ProductRetrieveUpdateDeleteView.as_view(),
        name="product_detail",
    ),
]
