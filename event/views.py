from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from datetime import datetime

from .models import Event
from .forms import EventForm

def index(request):
	"""Index displays all the events in most recent first"""
	events = Event.objects.all()
	# return render(request, 'event/index.html')
	return render(request, 'event/index.html', { 'events': events })

@login_required()
def make_event(request):
	"""Allows a logged in user to make an event"""
	if request.method == 'POST':
		form = EventForm(request.POST)
		if form.is_valid():
			form = form.save(commit=False)
			curr_user = request.user
			form.posted_by = curr_user
			form.created = datetime.now()
			form = form.save()
			return redirect(reverse('index'))
	else:
		form = EventForm()
	return render(request, 'event/new_event.html', {'form': form})

def view_event(request, pk):
	"""View all of an event's details"""
	event = Event.objects.get(pk=pk)
	return render(request, 'event/event.html', {'event': event}) 

def going_to_event(request, pk):
	"""Adds the request user to the list of users going to an event"""
	event = Event.objects.get(pk=pk)
	if request.user.event_set.filter(pk=pk).exists(): 
		return redirect(reverse('view event', kwargs={'pk': pk}))
	event.users.add(request.user)
	event.save()
	return redirect(reverse('view event', kwargs={'pk': pk}))



