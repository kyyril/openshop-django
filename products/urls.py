from django.urls import path
from .views import ProductListView, ProductDetailView

urlpatterns = [
    # Supports both /products and /products/ (Postman collection uses trailing slash)
    path("products/", ProductListView.as_view(), name="product-list"),
    path("products", ProductListView.as_view(), name="product-list-no-slash"),
    path("products/<uuid:pk>/", ProductDetailView.as_view(), name="product-detail"),
]
