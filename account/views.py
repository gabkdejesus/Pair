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
	events = request.user.event_set.all()
	return render(request, 'account/profile.html', {'events': events})

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


def update_profile(request, user_id):
	user = User.objects.get(pk=user_id)
	user.profile.bio = 'This user does not have a bio yet!'
	user.profile.gender = 'none'
	user.profile.birth_date = datetime.now()
	user.save()

