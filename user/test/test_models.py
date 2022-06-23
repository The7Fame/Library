from django.test import TestCase
from user.models import Profile
from django.contrib.auth.models import User


class UserRegistrationModelTest(TestCase):

	def test_can_registration(self):
		user = User.objects.create(username='user')
		Profile.objects.create(user=user)
		self.assertTrue(User.objects.all().filter(id=1))
		self.assertIn(User.objects.first().username,'user')
		self.assertTrue(Profile.objects.all().filter(id=1))