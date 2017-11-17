from django.shortcuts import render, render_to_response
from django.contrib.auth.decorators import login_required
from .models import Event

def index(request):
	"""Index displays all the sponsor events and user created events"""
	events = Event.objects.all()
	# return render(request, 'event/index.html')
	return render(request, 'event/index.html', { 'events': events })
