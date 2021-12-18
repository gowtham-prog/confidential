from django.shortcuts import render,HttpResponse,HttpResponseRedirect
from django.urls import reverse
from .models import *
from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.contrib.auth.decorators import login_required
import datetime

def index(request):
    return render(request,"dbs/index.html")