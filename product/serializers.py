from rest_framework import serializers

from .models import Product, Category, ProductImage


class CategorySerializer(serializers.ModelSerializer):
    product_category = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    # product_category = serializers.HyperlinkedRelatedField(
    #     many=True, view_name="product_detail", queryset=Product.objects.all()
    # )

    class Meta:
        model = Category
        fields = ["id", "title", "product_category"]


class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = ["id", "product", "image"]


class ProductSerializer(serializers.ModelSerializer):
    category = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    # product_category = CategorySerializer(many=True, read_only=True)
    images = ProductImageSerializer(many=True, read_only=True)
    uploaded_images = serializers.ListField(
        child=serializers.ImageField(
            max_length=1000000, allow_empty_file=True, use_url=False
        ),
        write_only=True,
    )

    class Meta:
        model = Product
        fields = [
            "id",
            "title",
            "description",
            "price",
            "weight",
            "location",
            "category",
            "image_url",
            "images",
            "uploaded_images",
        ]
        depth = 1

    def create(self, validated_data):
        uploaded_images = validated_data.pop("uploaded_images")
        product = Product.objects.create(**validated_data)
        for image in uploaded_images:
            newproduct_image = ProductImage.objects.create(product=product, image=image)
        return product


# class PageSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Page
#         fields = ["id", "title", "body", "slug", "featured_image", "created_on", "updated_on"]
