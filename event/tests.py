from django.test import TestCase
from django.contrib.auth.models import User
from event.models import Event
from category.models import Category
from datetime import datetime

class EventTest(TestCase):
	def setUp(self):
		self.user = User.objects.create(username='Gab')
		self.category1 = Category.objects.create(name='sports', desc='Games like basketball')
		self.category2 = Category.objects.create(name='music', desc='Music')
		self.event = Event.objects.create(id=1, name='UAAP', desc='Basketball games', 
			venue='BEG', start = datetime.now(), end = datetime.now(), 
			posted_by = self.user, category = [self.category1, self.category2])

	def test_event_name(self):
		"""Test the event's name"""
		self.assertEqual(self.event.name, 'UAAP')

	def test_event_categories(self):
		"""Test if the newly made event's categories matches setUp's"""
		category1 = self.event.category.all()[0]
		category2 = self.event.category.all()[1]
		self.assertEqual(category1.name, 'sports')
		self.assertEqual(category2.name, 'music')

	def test_event_user(self):
		"""Test the event's created by User"""
		user = User.objects.get(username='Gab')
		self.assertEqual(self.event.posted_by, user)



