from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import *
from django.contrib.auth.models import User
# Create your views here.

def member_login(request):
    if request.METHOD == 'POST':
        authenticate()

        pass
    return render(request, "")

@login_required
def member_dashboard(request):
    return render(request, "")

@login_required
def member_account(request):
    return render(request, "")

@login_required
def business_profile_edit(request):
    return render(request, "")

@login_required
def transaction_history(request):
    return render(request, "")

@login_required
def member_logout(request):
    logout(request)
    messages.error(request, 'Logged out successfully')
    return redirect()