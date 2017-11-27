from django import forms
from django.forms import widgets
from django.contrib.auth.models import User
from .models import Event
from account.models import Profile

class EventForm(forms.ModelForm):

	class Meta:
		model = Event
		fields = ('name', 'desc', 'venue', 'sponsored', 'start', 'end', 'category')

	def __init__(self, *args, **kwargs):
		super(EventForm, self).__init__(*args, **kwargs)
		self.fields['start'].widget = widgets.SelectDateWidget()
		self.fields['end'].widget = widgets.SelectDateWidget()

class ProfileForm(forms.ModelForm):
	class Meta:
		model = Profile
		fields = ('bio', 'birth_date', 'gender')