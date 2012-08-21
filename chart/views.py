
from chart.models import User, UserProfile
from chart.models import DailyVital, Medication
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
# import reportlab
# from reportlab.pdfgen import canvas




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
                return redirect("user_detail")
            else:
                state = "Your account is not active, please contact the site admin."
        else:
            state = "Your username and/or password were incorrect."
    return render(request, 'auth.html',{'state':state, 'username': username})


def logout_view(request):
    logout(request)
    return redirect("home")


@csrf_exempt
def registration(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            return redirect("home")
    else:
        form = UserCreationForm()
    return render_to_response("registration.html", {
        'form': form,
    })


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


def meds(request):
    if request.method == 'POST':
        print request.POST
        form = validators.MedsUpdateForm(request.POST)

        if form.is_valid():
            m = Medication()
            # print type(form.entered_at)
            m.medication = form.cleaned_data['medication']
            m.started_at = form.cleaned_data['started_at']
            m.stopped_at = form.cleaned_data['stopped_at']
            m.side_effects = form.cleaned_data['side_effects']
            m.prescribing_dr = form.cleaned_data['prescribing_dr']
            m.dosage = form.cleaned_data['dosage']
            m.comments = form.cleaned_data['comments']

            m.user = request.user
            m.save()

            return redirect("user_detail")
            pass

        else:
            medications = request.user.medication_set.all()
            return render(request, 'meds.html', {"med": meds, 
                "medications": medications, "form": form})
    else:
        form = validators.MedsUpdateForm()

        try:
            vitals = request.user.dailyvital_set.all()
            medications = request.user.medication_set.all()

        except User.DoesNotExist:
            raise Http404
        return render(request, 'meds.html', {"medications": medications, "form": form})




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

        except User.DoesNotExist:
            raise Http404
        return render(request, 'update.html', {"vitals": vitals, 
            "medications": medications,
            "form": form})


# broken
def download(request):
    response = HttpResponse(mimetype='application/pdf')
    response['Content-Disposition'] = 'attachment; filename=somefilename.pdf'
    p = canvas.Canvas(response)
    p.drawString(100, 100, "ALLLLLLL the datas!")
    p.showPage()
    p.save()
    return response








