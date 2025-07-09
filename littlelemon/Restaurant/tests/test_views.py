from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient
from Restaurant.models import Menu
from Restaurant.serializers import ModelSerializer


class MenuViewTest(TestCase):
    def setUp(self):
        self.client = APIClient()

        # Create data for test
        Menu.objects.create(title="Pasta", price=10.50, inventory=20)
        Menu.objects.create(title="Pizza", price=12.00, inventory=15)
        Menu.objects.create(title="Salad", price=8.75, inventory=25)

        # Create user
        from django.contrib.auth.models import User

        self.user = User.objects.create_user(username="testuser", password="testpass")
        self.client.force_authenticate(user=self.user)

    def test_getall(self):
        response = self.client.get("/restaurant/menu/")
        menu_items = Menu.objects.all()
        serializer = ModelSerializer(menu_items, many=True)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["results"], serializer.data)
