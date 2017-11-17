from django.test import TestCase
from django.core.urlresolvers import reverse
from django.urls import resolve
from django.contrib.auth.models import User
from datetime import datetime

from account.models import Profile

from account.forms import SignUpForm

from account.views import signup

class ProfileTests(TestCase):
	def setUp(self):
		"""Setup a user with inserted profile components"""
		self.u1 = User.objects.create(username='Gabby')
		self.u1.profile.bio = "I'm a female profile with inserted components"
		self.u1.profile.birth_date = datetime.now()
		self.u1.profile.gender = 'female'
		self.u1.profile.save()

	def test_components_profile(self):
		"""Test the inserted components profile"""
		profile = Profile.objects.get(bio="I'm a female profile with inserted components")
		self.assertEqual(self.u1.profile, profile)

	def test_components_profile_gender(self):
		"""Test the inserted components profile's gender"""
		self.assertEqual(self.u1.profile.gender, 'female')
	

class SignUpTests(TestCase):
	def setUp(self):
		url = reverse('signup')
		self.response = self.client.get(url)

	def test_signup_status_code(self):
		"""Test if /signup/ returns status 200"""
		self.assertEquals(self.response.status_code, 200)

	def test_signup_url_resolves_signup_view(self):
		"""Test if /signup/ returns the signup view"""
		view = resolve('/signup/')
		self.assertEquals(view.func, signup)

	def test_form_inputs(self):
		"""Test if the view contains five inputs: csrf, username, email, pass1 and 2"""
		self.assertContains(self.response, '<input', 5)
		self.assertContains(self.response, 'type="text"', 1)
		self.assertContains(self.response, 'type="email"', 1)
		self.assertContains(self.response, 'type="password"', 2)

class SignUpFormTests(TestCase):
	def test_form_has_fields(self):
		"""Test if SignUpForm still has the proper fields"""
		form = SignUpForm()
		expected = ['username', 'email', 'password1', 'password2']
		actual = list(form.fields)
		self.assertSequenceEqual(expected, actual)

class SuccessfulSignUpTests(TestCase):
	def setUp(self):
		url = reverse('signup')
		data = {
			'username': 'Gab',
			'email': 'gab@gmail.com',
			'password1': 'test',
			'password2': 'test',
		}
		self.response = self.client.post(url, data)
		self.home_url = reverse('index')

