
from chart.models import User, UserProfile
from chart.models import DailyVital
from django.http import HttpResponse
from django.template import Context, loader, RequestContext
from django.shortcuts import render_to_response, redirect, get_object_or_404, render 
from django.http import Http404
from django.contrib.auth import authenticate, login, logout
from django.core.context_processors import csrf
from django.views.decorators.csrf import csrf_exempt
from django.core import serializers                                  
import datetime, random, sha
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect
import validators


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
def detail(request):
    try:
    	current = request.user
    	vitals = current.dailyvital_set.all()
        json_vitals = serializers.serialize("json", vitals)
        medications = current.medication_set.all()
    	# current = User.objects.filter(id=user_id).one()
    except User.DoesNotExist:
    	raise Http404
    return render(request, 'detail.html', {'vitals': vitals, "medications": 
        medications, 'data': json_vitals})

@csrf_exempt
def update_info(request, user_id):
    if request.method == 'POST':
        date = request.POST.get('date')
        time = request.POST.get('time')
        try:
            current = User.objects.get(pk=user_id)
            vitals = current.dailyvital_set.all()
            medications = current.medication_set.all()
            form.save()
        except User.DoesNotExist:
          raise Http404
    return render(request, 'update.html',  {'current_user': current, 
        'vitals': vitals, "medications": medications,'id': user_id})


# this works kinda, does not push info into db or save it or any of that good stuff

def update(request):
    print request.user.username
    if request.method == 'POST':
        print request.POST
        form = validators.VitalsUpdateForm(request.POST)

        if form.is_valid():
            v = DailyVital()
            # print type(form.entered_at)
            v.entered_at = form.cleaned_data['entered_at']
            v.high_BGL = form.cleaned_data['high_BGL']
            v.low_BGL = form.cleaned_data['low_BGL']
            v.diet = form.cleaned_data['diet']
            v.activity = form.cleaned_data['activity']
            v.mood = form.cleaned_data['mood']
            v.comments = form.cleaned_data['comments']

            v.user = request.user
            v.save()

            return redirect("user_detail")
            # save to db
            pass

        else:
            vitals = request.user.dailyvital_set.all()
            medications = request.user.medication_set.all()
            return render(request, 'update.html', {"vitals": vitals, 
                "medications": medications, "form": form})


    else:
        form = validators.VitalsUpdateForm()

        try:
            vitals = request.user.dailyvital_set.all()
            medications = request.user.medication_set.all()
            # current = User.objects.filter(id=user_id).one()

        except User.DoesNotExist:
            raise Http404
        return render(request, 'update.html', {"vitals": vitals, 
            "medications": medications,
            "form": form})

def download(request,user_id):
	return HttpResponse("This is where you can export PHI in txt html or ccd format.")
