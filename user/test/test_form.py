from django.test import TestCase
from user.forms import RegisterForm


class UserRegistrationFormTest(TestCase):

	def test_registration_form(self):
		form_good = RegisterForm(data={'username':'user_1',
									   'password1':'qwerty_7B',
									   'password2':'qwerty_7B'})
		self.assertTrue(form_good.is_valid())


