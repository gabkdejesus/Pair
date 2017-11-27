from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login as auth_login
from datetime import datetime

from django.contrib.auth.models import User
from event.models import Event

from .forms import SignUpForm

@login_required
def profile(request):
	# Many to many relationship
	user = User.objects.filter(pk=request.user.id)
	events = Event.objects.filter(users__in=user)
	created_events = Event.objects.filter(posted_by=request.user)
	return render(request, 'account/profile.html', {'created_events': created_events, 'events': events})

def signup(request):
	if request.method == 'POST':
		form = SignUpForm(request.POST)
		if form.is_valid():
			user = form.save()
			auth_login(request, user)
			return redirect(reverse('index'))
	else:
		form = SignUpForm()
	return render(request, 'account/signup.html', {'form': form})

def view_profile(request, pk):
	"""View a user's profile"""
	user = User.objects.filter(pk=pk)
	events = Event.objects.filter(users__in=user)
	created_events = Event.objects.filter(posted_by=user)
	user = User.objects.get(pk=pk)
	return render(request, 'account/viewprofile.html', {'created_events': created_events, 'events': events, 'user': user})
