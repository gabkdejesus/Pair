from django.db import models
from django.contrib.auth.models import User

# App models
from category.models import Category

class Event(models.Model):
	name = models.CharField(max_length=255)
	desc = models.TextField(max_length=2000)
	venue = models.CharField(max_length=255)
	start = models.DateTimeField()
	end = models.DateTimeField()
	sponsored = models.BooleanField(default=False)
	posted_by = models.ForeignKey(User) 
	category = models.ManyToManyField(Category)
	
	def __str__ (self):
		return self.name
