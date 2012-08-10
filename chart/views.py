
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
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect


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


# this isnt working right.  
# @csrf_exempt
# def plz_login(request):
#     state = "Sorry you must be logged in to view this page."
#     username = password = ''
#     if request.POST:
#         username = request.POST.get('username')
#         password = request.POST.get('password')
#         print username, password
#         user = authenticate(username=username, password=password)
#         if user is not None:
#             if user.is_active:
#                 login(request, user)
#                 state = "You're successfully logged in!"
#                 return redirect("user_detail", user_id = user.id)
#             else:
#                 state = "Your account is not active, please contact the site admin."
#         else:
#            return render_to_response("registration.html", {
#         'form': form,})
#     return render_to_response('auth.html',{'state':state, 'username': username},
#         context_instance = RequestContext(request))

def logout_view(request, user_id):
    logout(request)
    return redirect("home")

@csrf_exempt
def registration(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            return HttpResponseRedirect("home")
    else:
        form = UserCreationForm()
    return render_to_response("registration.html", {
        'form': form,
    })



# user detailed main page
def detail(request, user_id):
    try:
    	current = User.objects.get(pk=user_id)
    	vitals = current.dailyvital_set.all()
        medications = current.medications_set.all()
    	# current = User.objects.filter(id=user_id).one()
    except User.DoesNotExist:
    	raise Http404
    return render_to_response('detail.html', {'current_user': current, 'vitals': vitals, "medications": medications,'id': user_id})

@csrf_exempt
def update_info(request, user_id):
    if request.method == 'POST':
        date = request.POST.get('date')
        time = request.POST.get('time')
        print date, time
        try:
          current = User.objects.get(pk=user_id)
          vitals = current.dailyvital_set.all()
          medications = current.medications_set.all()
        except User.DoesNotExist:
          raise Http404
    return render_to_response('update.html',  {'current_user': current, 'vitals': vitals, "medications": medications,'id': user_id},
                                context_instance=RequestContext(request))


# this works kinda, does not push info into db or save it or any of that good stuff

def update(request, user_id):
    try:
    	current = User.objects.get(pk=user_id)
    	vitals = current.dailyvital_set.all()
        medications = current.medications_set.all()
    	# current = User.objects.filter(id=user_id).one()
    except User.DoesNotExist:
    	raise Http404
    return render_to_response('update.html', {"current_user": current, "vitals": vitals, "medications": medications, "id": user_id})

def download(request,user_id):
	return HttpResponse("This is where you can export PHI in txt html or ccd format.")
