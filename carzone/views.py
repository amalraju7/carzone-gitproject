from django.shortcuts import  HttpResponse,render
from django.contrib import messages
from django.template import RequestContext


from django.core.mail import send_mail
from django.contrib.auth.models import User


# Create your views here.
def my_model(request):
     r = render(request,'admin/myapp/my_model.html')
     return HttpResponse(r)
