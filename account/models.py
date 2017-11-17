from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Profile(models.Model):
	"""Makes a profile with additional details for the user. Code is from Vitor Freitas"""
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	bio = models.TextField(max_length=2000, blank=True)
	birth_date = models.DateField(null=True, blank=True)
	male = 'male'
	female = 'female'
	other = 'other'
	none = 'none'
	GENDER_CHOICES = (
		(male, 'male'),
		(female, 'female'),
		(other, 'other'),
		(none, 'none'),
	)
	gender = models.CharField(max_length=6, choices=GENDER_CHOICES)

#Hook functions to User.save and User.create, so that profile is also updated
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
	if created:
		Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
	instance.profile.save()