from django.db import models

class Category(models.Model):
	name = models.CharField(max_length=255)
	desc = models.TextField(max_length=2000)
	
	def __str__ (self):
		return self.name

	class Meta:
		verbose_name = 'Category'
		verbose_name_plural = 'Categories'