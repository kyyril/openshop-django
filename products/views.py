from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Product
from .serializers import ProductSerializer


class ProductListView(APIView):
    """
    GET  /products        – list all non-deleted products (supports ?name= and ?location= filters)
    POST /products        – create a new product
    """

    def get(self, request):
        queryset = Product.objects.filter(is_delete=False)

        name = request.query_params.get("name")
        location = request.query_params.get("location")

        if name:
            queryset = queryset.filter(name__icontains=name)
        if location:
            queryset = queryset.filter(location__icontains=location)

        serializer = ProductSerializer(queryset, many=True, context={"request": request})
        return Response({"products": serializer.data}, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = ProductSerializer(data=request.data, context={"request": request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProductDetailView(APIView):
    """
    GET    /products/:id/  – retrieve a product (including soft-deleted ones)
    PUT    /products/:id/  – update a product
    DELETE /products/:id/  – soft-delete a product
    """

    def _get_object(self, pk):
        """Return product or None; includes soft-deleted records for GET."""
        try:
            return Product.objects.get(pk=pk)
        except Product.DoesNotExist:
            return None

    def _get_active_object(self, pk):
        """Return only non-deleted product or None (used for PUT/DELETE)."""
        try:
            return Product.objects.get(pk=pk, is_delete=False)
        except Product.DoesNotExist:
            return None

    def get(self, request, pk):
        product = self._get_object(pk)
        if product is None:
            return Response({"detail": "Not found."}, status=status.HTTP_404_NOT_FOUND)
        serializer = ProductSerializer(product, context={"request": request})
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        product = self._get_active_object(pk)
        if product is None:
            return Response({"detail": "Not found."}, status=status.HTTP_404_NOT_FOUND)
        serializer = ProductSerializer(product, data=request.data, context={"request": request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        product = self._get_active_object(pk)
        if product is None:
            return Response({"detail": "Not found."}, status=status.HTTP_404_NOT_FOUND)
        # Soft delete – flag the record instead of removing it
        product.is_delete = True
        product.save()
        return Response(status=status.HTTP_204_NO_CONTENT)
