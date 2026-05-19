from django.test import TestCase
from django.contrib.auth.models import User

from apps.accounts.models import Profile


class ProfileTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='test', password='12345678')
        self.profile = self.user.profile
        self.profile.city = 'Minsk'
        self.profile.save()

    def test_profile_created(self):
        self.assertEqual(self.profile.user.username, 'test')

    def test_profile_city(self):
        self.assertEqual(self.profile.city, 'Minsk')
