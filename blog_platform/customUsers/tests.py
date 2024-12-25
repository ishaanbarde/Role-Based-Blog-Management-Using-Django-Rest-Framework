from django.urls import reverse
from django.contrib.auth import get_user_model

from rest_framework.test import APITestCase
from rest_framework import status
from .models import CustomUser

class AuthTests(APITestCase):
    def test_register_user(self):

        url = reverse('register')
        data = {
            "username": "testuser",
            "password": "testpass123",
            "email": "testuser@example.com"
        }

        response = self.client.post(url, data)

        # self.assertEqual(response.status_code)
        user = get_user_model().objects.get(username='testuser')
        self.assertNotEqual(user.password, 'testpass123')
        self.assertEqual(user.role, 'Owner')
        self.assertEqual(user.email, 'testuser@example.com')
    
    def test_login_user(self):
        user = CustomUser.objects.create_user(username="testuser", password="testpass123", email="test@example.com")
        url = reverse('login')  # /users/login/
        data = {"username": "testuser", "password": "testpass123"}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class UserManagementTests(APITestCase):
    def setUp(self):
        self.owner = CustomUser.objects.create_user(username="owner", password="ownerpass", role="Owner")
        self.client.force_authenticate(user=self.owner)

    def test_create_user_by_owner(self):
        url = reverse('createUser')
        data = {
            "username": "adminuser",
            "password": "adminpass",
            "role": "Admin"
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_list_users(self):
        url = reverse('userlist')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_user_role(self):
        user = CustomUser.objects.create_user(username="memberuser", password="memberpass", role="Member")
        url = reverse('updateRole', kwargs={'user_id': user.id})  # /users/owner/<user_id>/updateRole/
        data = {"role": "Admin"}
        response = self.client.put(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
