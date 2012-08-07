
from chart.models import User, UserProfile
from chart.models import DailyVital
from django.http import HttpResponse
from django.template import Context, loader, RequestContext
from django.shortcuts import render_to_response, redirect, get_object_or_404, render 
from django.http import Http404
from django.contrib.auth import authenticate, login, logout
from django.core.context_processors import csrf
from django.views.decorators.csrf import csrf_exempt                                          
import datetime, random, sha
# from chart.forms import UserProfileForm, DailyVitalForm
# from django.core.mail import send_mail
# from django.core.urlresolvers import reverse
# from django.template import RequestContext
# from django.contrib.auth.tokens import default_token_generator
# from django.contrib.sites.models import Site




def login_view(request):
    state = "Please log in below..."
    username = password = ''
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        print username, password
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                state = "You're successfully logged in!"
                return redirect("user_detail", user_id = user.id)
            else:
                state = "Your account is not active, please contact the site admin."
        else:
            state = "Your username and/or password were incorrect."
    return render_to_response('auth.html',{'state':state, 'username': username},
    	context_instance = RequestContext(request))

def logout_view(request):
    logout(request)
    return redirect("home")



# tabled for another day, sign up for new users
def registration(request):
    return render_to_response("registration.html")



# user detailed main page
def detail(request, user_id):
    try:
    	current = User.objects.get(pk=user_id)
    	vitals = current.dailyvital_set.all()
    	# current = User.objects.filter(id=user_id).one()
    except User.DoesNotExist:
    	raise Http404
    return render_to_response('detail.html', {'current_user': current, 'vitals': vitals, 'id': user_id})

@csrf_exempt
def update_info(request, user_id):
    print request.method
    if request.method == 'POST':
        date = request.POST.get('date')
        time = request.POST.get('time')
        print date, time
        try:
          current = User.objects.get(pk=user_id)
          vitals = current.dailyvital_set.all()
        except User.DoesNotExist:
          raise Http404
    return render_to_response('detail.html',  {'current_user': current, 'vitals': vitals, 'id': user_id},
                                context_instance=RequestContext(request))


# this works kinda, does not push info into db or save it or any of that good stuff

def update(request, user_id):
    try:
    	current = User.objects.get(pk=user_id)
    	vitals = current.dailyvital_set.all()
    	# current = User.objects.filter(id=user_id).one()
    except User.DoesNotExist:
    	raise Http404
    return render_to_response('update.html', {'current_user': current, "vitals": vitals, 'id': user_id})

def download(request,user_id):
	return HttpResponse("This is where you can export PHI in txt html or ccd format.")
