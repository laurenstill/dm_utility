# Create your page views here.
from chart.models import User
from django.http import HttpResponse
from django.template import Context, loader

def index(request):
    return HttpResponse("This is the front page with info/login/etc.  Yay.")


# 
def detail(request, user_id):
    return HttpResponse("You're looking user #%s's dashboard now!" % user_id)
    info = User.objects.all()
    t = loader.get_template('user/detail.html')  
    c = Context({
        'Info': info,
    })
    return HttpResponse(t.render(c))


def update(request, user_id):
    return HttpResponse("You're looking user #%s' update data-entry page" % user_id)

def download(request,user_id):
	return HttpResponse("This is where you can export PHI in txt html or ccd format.")
