from rest_framework.test import APITestCase, APIRequestFactory
from django.urls import reverse
from rest_framework import status
from urllib.parse import urlencode

# from .views import ProductListCreateView, ProductRetrieveUpdateDeleteView, CategoryListCreateView, CategoryRetrieveUpdateDeleteView
from django.contrib.auth import get_user_model


User = get_user_model()


class ProductListCreateTestCase(APITestCase):
    def setUp(self):
        self.urls = reverse("list_product")

    def authenticate(self):
        self.client.post(
            reverse("signup"),
            {
                "first_name": "Kingss",
                "last_name": "Sdikaa",
                "email": "adikaking@gmail.com",
                "password": "password123",
                "phone": "08029616767",
                "terms": True,
            },
        )

        response = self.client.post(
            reverse("login"),
            {
                "email": "adikaking@gmail.com",
                "password": "password123",
            },
        )

        print(response.data)

        token = response.data["Token"]["access"]

        print(token)

        self.client.credentials(HTTP_AUTHORIZATION=f"Bearer {token}")

    def test_list_product(self):
        response = self.client.get(self.urls)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_product(self):
        self.authenticate()

        sample_data = urlencode(
            {
                "title": "Test Title",
                "description": "Test Description",
                "price": "Test Price",
                "weight": "Test Weight",
                "location": "Test Location",
                # "product_category": {"Test Product Category"},
                "image_url": "Test Image URL",
                # "images": "Test Images",
                "uploaded_images": [
                    {
                        "id": 1,
                        "product": 9,
                        "image": "http://127.0.0.1:8000/media/images/meebol-onlinestore_banner_b5AtjYZ.png",
                    },
                ],
            }
        )

        response = self.client.post(reverse("list_product"), sample_data)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        # self.assertEqual(response.data["title"], sample_data["title"])
