from chart.models import User
from chart.models import DailyVitals
from django.contrib import admin

admin.site.register(User)
# admin.site.register(DailyVitals)

class DailyVitalsAdmin(admin.ModelAdmin):
	list_display = ('user', 'entered_at')

admin.site.register(DailyVitals, DailyVitalsAdmin)



