from django.shortcuts import render_to_response
#from django.template.context import RequestContext
#from scrumboard.core.decorators import render_template
from scrumboard.settings import STATIC_URL
from django.contrib.auth.decorators import login_required

@login_required
def app(request):
    return render_to_response("board/app.html",{"STATIC_URL":STATIC_URL})

@login_required
def home(request):
    return render_to_response("index.html",{"STATIC_URL":STATIC_URL})