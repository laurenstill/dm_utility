from chart.models import UserProfile, Medication
from chart.models import DailyVital
from django.contrib import admin

admin.site.register(UserProfile)
# admin.site.register(DailyVitals)

class DailyVitalAdmin(admin.ModelAdmin):
	list_display = ('user', 'entered_at')

class MedicationAdmin(admin.ModelAdmin):
	list_display = ('user', 'medication')

admin.site.register(DailyVital, DailyVitalAdmin)
admin.site.register(Medication)
