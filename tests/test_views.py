from django.test import TestCase
from restaurant.models import Menu
from restaurant.serializers import MenuItemSerializer
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User

class MenuViewTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.token = Token.objects.create(user=self.user)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)
        self.menu1 = Menu.objects.create(title="Pizza", price=10.99, inventory=5)
        self.menu2 = Menu.objects.create(title="Burger", price=8.99, inventory=10)
        self.menu3 = Menu.objects.create(title="Pasta", price=9.99, inventory=7)

    def test_getall(self):
        response = self.client.get(reverse('menu-list'))
        menus = Menu.objects.all()
        serializer = MenuItemSerializer(menus, many=True)
        self.assertEqual(response.data, serializer.data)