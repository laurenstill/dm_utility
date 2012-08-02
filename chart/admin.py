from chart.models import UserProfile
from chart.models import DailyVital
from django.contrib import admin

admin.site.register(UserProfile)
# admin.site.register(DailyVitals)

class DailyVitalAdmin(admin.ModelAdmin):
	list_display = ('user', 'entered_at')

admin.site.register(DailyVital, DailyVitalAdmin)



