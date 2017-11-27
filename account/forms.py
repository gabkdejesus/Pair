from django import forms
from django.forms import widgets
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile

class SignUpForm(UserCreationForm):
	email = forms.CharField(max_length=254, required=True, widget=forms.EmailInput())
	class Meta:
		model = User
		fields = ('username', 'email', 'password1', 'password2')

class ProfileForm(forms.ModelForm):
	class Meta:
		model = Profile
		fields = ('bio', 'birth_date', 'gender')

	def __init__(self, *args, **kwargs):
		super(ProfileForm, self).__init__(*args, **kwargs)
		self.fields['birth_date'].widget = widgets.SelectDateWidget()