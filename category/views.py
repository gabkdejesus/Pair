from django.shortcuts import render, redirect
from django.urls import reverse

from .models import Category
from event.models import Event

def index(request):
	"""View all the categories available"""
	categories = Category.objects.all().order_by('name')
	return render(request, 'category/index.html', {'categories': categories})

def view_category(request, pk):
	"""View all of the events under a category"""
	category = Category.objects.get(pk=pk)
	events = Event.objects.filter(category = category)
	return render(request, 'category/category.html', {'category': category, 'events': events})