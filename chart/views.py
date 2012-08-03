# Create your page views here.
from chart.models import User, UserProfile
from chart.models import DailyVital
from django.http import HttpResponse
from django.template import Context, loader, RequestContext
from django.shortcuts import render_to_response, redirect, get_object_or_404
from django.http import Http404
from django.contrib.auth import authenticate, login, logout
from django.core.context_processors import csrf
# import datetime, random, sha
# from django.core.mail import send_mail
# from chart.forms import RegistrationForm



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

# def register(request):
#     if request.user.is_authenticated():
#         # They already have an account; don't let them register again
#         return render_to_response('register.html', {'has_account': True})
#     manipulator = RegistrationForm()
#     if request.POST:
#         new_data = request.POST.copy()
#         errors = manipulator.get_validation_errors(new_data)
#         if not errors:
#             # Save the user                                                                                                                                                 
#             manipulator.do_html2python(new_data)
#             new_user = manipulator.save(new_data)
            
#             # Build the activation key for their account                                                                                                                    
#             salt = sha.new(str(random.random())).hexdigest()[:5]
#             activation_key = sha.new(salt+new_user.username).hexdigest()
#             key_expires = datetime.datetime.today() + datetime.timedelta(2)
            
#             # Create and save their profile                                                                                                                                 
#             new_profile = UserProfile(user=new_user,
#                                       activation_key=activation_key,
#                                       key_expires=key_expires)
#             new_profile.save()
            
#             # Send an email with the confirmation link                                                                                                                      
#             email_subject = 'Your new example.com account confirmation'
#             email_body = "Hello, %s, and thanks for signing up for an \                                                                                                     
# example.com account!\n\nTo activate your account, click this link within 48 \                                                                                               
# hours:\n\nhttp://example.com/accounts/confirm/%s" % (
#                 new_user.username,
#                 new_profile.activation_key)
#             send_mail(email_subject,
#                       email_body,
#                       'accounts@example.com',
#                       [new_user.email])
            
#             return render_to_response('register.html', {'created': True})
#     else:
#         errors = new_data = {}
#     form = forms.FormWrapper(manipulator, new_data, errors)
#     return render_to_response('register.html', {'form': form})

# def confirm(request, activation_key):
#     if request.user.is_authenticated():
#         return render_to_response('confirm.html', {'has_account': True})
#     user_profile = get_object_or_404(UserProfile,
#                                      activation_key=activation_key)
#     if user_profile.key_expires < datetime.datetime.today():
#         return render_to_response('confirm.html', {'expired': True})
#     user_account = user_profile.user
#     user_account.is_active = True
#     user_account.save()
#     return render_to_response('confirm.html', {'success': True})





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
    try:
    	current = User.objects.get(pk=user_id)
    	vitals = current.dailyvital_set.all()
    	# current = User.objects.filter(id=user_id).one()
    except User.DoesNotExist:
    	raise Http404
    return render_to_response('update.html', {'current_user': current, "vitals": vitals})

def download(request,user_id):
	return HttpResponse("This is where you can export PHI in txt html or ccd format.")
