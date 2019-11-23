from django.test import TestCase
from django.contrib.auth.models import User
# Create your tests here.

class ViewTests(TestCase):

    def test_view_login(self):
        username = 'test_user'
        password = 'password'
        user = User.objects.create_user(username=username, password=password)
        self.assertTrue(User.objects.filter(username=username).exists())
