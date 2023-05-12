from django.urls import path

from.views import PageListCreateView, PageRetrieveUpdateDeleteView

urlpatterns = [
    path("", PageListCreateView.as_view(), name="list_pages"),
    path("<slug:slug>/", PageRetrieveUpdateDeleteView.as_view(), name="page_detail"),
]