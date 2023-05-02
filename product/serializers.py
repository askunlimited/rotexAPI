from rest_framework import serializers

from .models import Product, Category, ProductImage


class CategorySerializer(serializers.ModelSerializer):
    title = serializers.CharField(max_length=50)
    # description = serializers.CharField(max_length=255)
    # created_on = serializers.DateTimeField()
    # updated_on = serializers.DateTimeField()

    class Meta:
        model = Category
        fields = ["title", "description"]


class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = ["id", "product", "image"]


class ProductSerializer(serializers.ModelSerializer):
    product_category = CategorySerializer(many=True, read_only=True)
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
            "title",
            "description",
            "price",
            "weight",
            "location",
            "product_category",
            "image_url",
            "images",
            "uploaded_images",
        ]
        depth = 1

    def create(self, validated_data):
        product_category = validated_data.pop("product_category")
        product = Product.objects.create(**validated_data)
        for category in product_category:
            Category.objects.create(product=product, **category)
        return product


    def create(self, validated_data):
        uploaded_images = validated_data.pop("uploaded_images")
        product = Product.objects.create(**validated_data)
        for image in uploaded_images:
            newproduct_image = ProductImage.objects.create(product=product, image=image)
        return product
