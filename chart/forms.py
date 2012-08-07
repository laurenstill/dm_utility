
from django import forms
from models import UserProfile
from models import DailyVital




class UserProfileForm(forms.Form):
	user = forms.OneToOneField(User, unique=True)
	birthday = forms.DateField(null = True, blank = True)
	updated_at = forms.DateTimeField(default=datetime.datetime.utcnow)
	phone_number = forms.IntegerField(max_length=15) 

	def __unicode__(self):
		return self.forms.username 


def update_user(sender, instance, created, **kwargs):
	if created:
		UserProfileForm.objects.create(user=instance)

post_save.connect(update_user, sender=User)



class DailyVitalForm(forms.Form):
	user =  form.ModelChoiceField(queryset=User.objects.all())
	entered_at = form.DateTimeField()
	high_BGL = form.IntegerField()
	low_BGL = form.IntegerField()
	diet = form.IntegerField()
	activity = form.IntegerField()
	mood = form.IntegerField()
	comments = form.CharField(blank = True, max_length = 500)
	####outside the realm of everyday charting, but still included in model on sidebar
	weight = form.IntegerField(blank = True)
	systolic = form.IntegerField(blank = True)
	diastolic = form.IntegerField(blank = True)
	medications = form.CharField(blank = True, max_length = 300)

	def __unicode__(self):
		return self.user.username




# right now two main goals, user registration, user daily/tracked input, and user additional input.
# ok, three, but whateves 


# current big issues:
# register new users
# have user add/update their daily tracked information
# have users updat information that is profile related 
# date/time in update feilds auto fill untless otherwise specified
# download and/or print information logged
# 
# 
# styling shit, design
# hover on chart still displaying all comments, instead of applicable comments