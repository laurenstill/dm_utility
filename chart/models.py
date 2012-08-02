from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
import datetime

class UserProfile(models.Model):
	user = models.OneToOneField(User)
	birthday = models.DateField(null = True, blank = True)
	updated_at = models.DateTimeField(default=datetime.datetime.utcnow)
	phone_number = models.CharField(max_length = 15)  #assigned phone number for emg contact
	
	def __unicode__(self):
		return self.user.username

def create_user_profile(sender, instance, created, **kwargs):
	if created:
		UserProfile.objects.create(user=instance)

post_save.connect(create_user_profile, sender=User)

class DailyVital(models.Model):
	user =  models.ForeignKey(User)
	entered_at = models.DateTimeField()
	high_BGL = models.IntegerField()
	low_BGL = models.IntegerField()
	diet = models.IntegerField()
	activity = models.IntegerField()
	mood = models.IntegerField()
	comments = models.CharField(max_length = 500)
	####outside the realm of everyday charting, but still included in model on sidebar
	weight = models.IntegerField()
	systolic = models.IntegerField()
	diastolic = models.IntegerField()
	medications = models.CharField(blank = True, max_length = 300)

	def __unicode__(self):
		# return "%s's Vitals" %(self.user.name)
		return self.user.username

