from rest_framework import serializers
from .models import Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = [
            "id",
            "name",
            "shop",
            "price",
            "sku",
            "description",
            "location",
            "discount",
            "category",
            "stock",
            "is_available",
            "picture",
            "is_delete",
        ]
        read_only_fields = ["id", "is_delete"]

    def to_representation(self, instance):
        """Append HATEOAS _links to each product representation."""
        representation = super().to_representation(instance)
        request = self.context.get("request")

        if request is not None:
            base_url = request.build_absolute_uri("/")
            base_url = base_url.rstrip("/")
        else:
            base_url = ""

        product_id = str(instance.id)
        representation["_links"] = [
            {
                "rel": "self",
                "href": f"{base_url}/products",
                "action": "POST",
                "types": ["application/json"],
            },
            {
                "rel": "self",
                "href": f"{base_url}/products/{product_id}/",
                "action": "GET",
                "types": ["application/json"],
            },
            {
                "rel": "self",
                "href": f"{base_url}/products/{product_id}/",
                "action": "PUT",
                "types": ["application/json"],
            },
            {
                "rel": "self",
                "href": f"{base_url}/products/{product_id}/",
                "action": "DELETE",
                "types": ["application/json"],
            },
        ]
        return representation
