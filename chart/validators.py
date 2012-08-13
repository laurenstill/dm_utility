from django import forms


class VitalsUpdateForm(forms.Form):
	entered_at = forms.DateTimeField(required = True, label="Enter a date")
	high_BGL = forms.IntegerField(required = True, min_value = 50, max_value = 300, 
		label="Blood Glucose Daily High")
	low_BGL = forms.IntegerField(required = True, min_value = 50, max_value = 300,
		label="Bloog Glucose Daily Low")
	diet = forms.IntegerField(required = True, min_value = 1, max_value = 10,
		label="Diet Quality (1-10)")
	activity = forms.IntegerField(required = True, min_value = 1, max_value = 10,
		label="Activity Level (1-10)")
	mood = forms.IntegerField(required = True, min_value = 1, max_value = 10,
		label="Mood (1-10)")
	comments = forms.CharField(required=False, label= "Comments")
