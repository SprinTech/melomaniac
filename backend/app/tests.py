from django.test import TestCase
from django.urls import reverse
from .models import User

# Test related to User.
class UserTest(TestCase):

    def setUp(self):
        self.user = User.objects.create(username=f"User 1", email=f"user1.gmail.com", password=f"password1")

    def test_get_user_list(self):
        response = self.client.get(reverse("user-list"))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 1)

    def test_get_user(self):
        response = self.client.get(reverse("user-detail", kwargs={'pk': self.user.pk}))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['username'], 'User 1')

    def test_create_user(self):
        data = {'username': 'User 2', 'password': 'password2', 'email': 'user29@gmail.com'}
        url = reverse('user-list')
        response = self.client.post(url, data=data, content_type='application/json')
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.data['username'], 'User 2')

    def test_patch_user(self):
        data = {'username': 'newUser'}
        url = reverse("user-detail", kwargs={'pk': self.user.pk})
        response = self.client.patch(url, data=data, content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['username'], 'newUser')

    def test_update_user(self):
        data = {'username': 'newUser', 'password': 'newPassword', 'email': 'newemail@gmail.com'}
        url = reverse("user-detail", kwargs={'pk': self.user.pk})
        response = self.client.put(url, data=data, content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['password'], 'newPassword')

    def test_delete_user(self):
        response = self.client.delete(reverse("user-detail", kwargs={'pk': self.user.pk}))
        self.assertEqual(response.status_code, 204)
    