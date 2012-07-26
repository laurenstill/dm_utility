from django.db import models

# Create your models here...

class User(models.Model):
	registered_date = models.DateTimeField()
	# user_id = models.IntegerField()
	birthday = models.DateField()
	email = models.CharField(max_length = 200)
	name = models.CharField(max_length = 60)
	#followers =  #hu, how do i do this? probably a separate class
	updated_at = models.DateTimeField()
	phone_number = models.CharField(max_length = 15)  #assigned phone number for emg contact

	def __unicode__(self):
		return self.User


class DailyVitals(models.Model):
	entered_at = models.DateTimeField()
	user =  models.ForeignKey(User)
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
	medications = models.CharField(max_length =300)

	def __unicode__(self):
		return self.DailyVitals





