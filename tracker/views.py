from django.shortcuts import render,redirect
from django.http import HttpResponse,Http404,HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
# from .models import *
# from .email import *
# from .forms import *
from decouple import config,Csv
import datetime as dt
from django.http import JsonResponse
import json
from django.db.models import Q
from django.contrib.auth.models import User

from rest_framework.response import Response
from rest_framework.views import APIView
# from .serializer import

import pyrebase
from django.shortcuts import render

# Create your views here.

config = {
    'apiKey': "AIzaSyBvoCO76pCaX1_DfoZgloCD-qAf4ySgC70",
    'authDomain': "transport-tracke-1543909006227.firebaseapp.com",
    'databaseURL': "https://transport-tracke-1543909006227.firebaseio.com",
    'projectId': "transport-tracke-1543909006227",
    'storageBucket': "transport-tracke-1543909006227.appspot.com",
    'messagingSenderId': "772725955306"
}
firebase = pyrebase.initialize_app(config)
auth = firebase.auth()

def singIn(request):
    return render(request, "signin.html")

def postsign(request):
    email=request.POST.get('email')
    passw = request.POST.get("pass")
    try:
        user = auth.sign_in_with_email_and_password(email,passw)
        return render(request, "welcome.html",{"e":email})
    except:
        message = "invalid cerediantials"
        return render(request,"signin.html",{"msg":message})
        print(user)


def index(request):
    # TODO: move this token to Django settings from an environment variable
    # found in the Mapbox account settings and getting started instructions
    # see https://www.mapbox.com/account/ under the "Access tokens" section
    mapbox_access_token = 'pk.eyJ1IjoiZG9uYWxka2lwbGFnYXQiLCJhIjoiY2pwOWs1cmx1MjRmazNrcGhyOHRxd2o4biJ9.NECvniOLKO4L14WCg-x_VQ'
    return render(request, 'trial.html',{ 'mapbox_access_token': mapbox_access_token })
