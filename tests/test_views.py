from django.contrib.auth.models import User
from django.test import TestCase, Client
from rest_framework.test import APIClient

from restaurant.models import MenuItem
from restaurant.serializers import MenuItemSerializer

class MenuViewTest(TestCase):
    def setUp(self):
        self.client = Client()

        self.credentials = {'username': 'testuser', 'password': 'Pass@123'}
        User.objects.create_user(**self.credentials)

        MenuItem.objects.create(title='IceCream', price=80, inventory=100)
        MenuItem.objects.create(title='Pizza', price=200, inventory=100)

        self.client.login(username='testuser', password='Pass@123')

    def test_getall(self):
        items = MenuItem.objects.all()
        serializer = MenuItemSerializer(data=items, many=True)
        serializer.is_valid()
        response = self.client.get('/api/menu-items/')
        self.assertEquals(serializer.data, response.json())
