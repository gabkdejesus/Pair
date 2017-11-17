from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login as auth_login
from datetime import datetime

from django.contrib.auth.models import User

from .forms import SignUpForm

def signup(request):
	if request.method == 'POST':
		form = SignUpForm(request.POST)
		if form.is_valid():
			user = form.save()
			auth_login(request, user)
			return redirect('index')
	else:
		form = SignUpForm()
	return render(request, 'account/signup.html', {'form': form})


def update_profile(request, user_id):
	user = User.objects.get(pk=user_id)
	user.profile.bio = 'This user does not have a bio yet!'
	user.profile.gender = 'none'
	user.profile.birth_date = datetime.now()
	user.save()
