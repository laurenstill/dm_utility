# Create your page views here.
from chart.models import User
from chart.models import DailyVital
from django.http import HttpResponse
from django.template import Context, loader, RequestContext
from django.shortcuts import render_to_response, redirect
from django.http import Http404
from django.contrib.auth import authenticate, login, logout
from django.core.context_processors import csrf



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


# user detailed main page
def detail(request, user_id):
    try:
    	current = User.objects.get(pk=user_id)
    	vitals = current.dailyvital_set.all()
    	# current = User.objects.filter(id=user_id).one()
    except User.DoesNotExist:
    	raise Http404
    return render_to_response('detail.html', {'current_user': current, "vitals": vitals})


def update(request, user_id):
    return HttpResponse("You're looking user #%s' update data-entry page" % user_id)

def download(request,user_id):
	return HttpResponse("This is where you can export PHI in txt html or ccd format.")
