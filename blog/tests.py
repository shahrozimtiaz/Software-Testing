from django.test import TestCase
from django.contrib.auth.models import User
from .models import Post
# Create your tests here.

class ViewTests(TestCase):

    def test_view_login(self):
        username = 'test_user'
        password = 'password'
        User.objects.create_user(username=username, password=password)
        self.assertTrue(User.objects.filter(username=username).exists())

    def test_view_makingPost(self):
        username = 'test_user'
        password = 'password'
        user = User.objects.create_user(username=username, password=password)
        self.assertTrue(User.objects.filter(username=username).exists())
        title = 'test_post'
        postDec = 'This is the post description'
        post = Post(user=user,title=title,post=postDec)
        post.save()
        self.assertTrue(Post.objects.filter(user=user).exists())
