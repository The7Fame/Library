from django.test import TestCase
from user.views import register_view, profile_view, profile_edit_view
from django.contrib.auth import views as auth_views
from django.contrib.auth.models import User
from user.models import Profile


class UserRegistrationTest(TestCase):

	def test_proper_register_view(self):
		response = self.client.get('/user/register/')
		self.assertTemplateUsed(response, 'user/register.html')
		self.assertEqual(response.status_code, 200)
		self.assertContains(response, 'Create')


class UserLoginViewTest(TestCase):

	def test_registered_user_login_view(self):
		response = self.client.get('/user/login/')
		self.assertEqual(response.status_code, 200)
		self.assertTemplateUsed(response, 'registration/login.html')


class UserProfileViewTest(TestCase):
	def setUp(self):
		self.credentials = {'username':'user', 'password':'qwerty'}
		self.user = User.objects.create_user(username='user')
		self.user.set_password('qwerty')
		self.user.save()
		self.profile = Profile.objects.create(user=self.user, date_of_birth=None,
				city='default')
		self.client.login(username='user', password='qwerty')

	def test_can_see_user_profile(self):
		response = self.client.get(f'/user/{self.user.pk}')
		self.assertEqual(response.status_code, 200)
		self.assertTemplateUsed(response, 'user/profile.html')
		self.assertIn(f'{self.profile.user.username}', response.content.decode())

	def test_loginned_user_can_see_another_user_profile(self):
		another_user = User.objects.create_user(username='user_2')
		another_user.set_password('qwerty')
		another_user.save()
		another_profile = Profile.objects.create(user=another_user, date_of_birth=None,
				city='default')
		response = self.client.get(f'/user/{another_user.pk}')
		self.assertEqual(response.status_code, 200)
		self.assertIn(f'{another_profile.user.username}', response.content.decode())

	def test_can_see_user_edit_profile(self):
		response = self.client.get(f'/user/edit/{self.user.pk}' )
		self.assertEqual(response.status_code, 200)
		self.assertTemplateUsed(response, 'user/profile_edit.html')
		self.assertIn(f'{self.user.username}', response.content.decode())

	def test_can_change_profile(self):
		response = self.client.post(f'/user/edit/{self.user.pk}', data={
			'city': 'not_default',
			'first_name': 'first_q',
			'last_name': 'last_q'})
		self.assertEqual(response.status_code, 302)
		self.assertRedirects(response, f'/user/{self.user.pk}')
		self.profile.refresh_from_db()
		self.user.refresh_from_db()
		self.assertEqual(self.profile.city,'not_default')
		self.assertEqual(self.user.first_name,'first_q')
		self.assertEqual(self.user.last_name,'last_q')