# Create your page views here.
from chart.models import User
from chart.models import DailyVitals
from django.http import HttpResponse
from django.template import Context, loader
from django.shortcuts import render_to_response
from django.http import Http404

def index(request):
    return HttpResponse("This is the front page with info/login/etc.  Yay.")


# user detailed main page
def detail(request, user_id):
    try:
    	current = User.objects.get(pk=user_id)
    	vitals = current.dailyvitals_set.all()
    	# current = User.objects.filter(id=user_id).one()
    except User.DoesNotExist:
    	raise Http404
    return render_to_response('detail.html', {'current_user': current, "vitals": vitals})


def update(request, user_id):
    return HttpResponse("You're looking user #%s' update data-entry page" % user_id)

def download(request,user_id):
	return HttpResponse("This is where you can export PHI in txt html or ccd format.")
