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

# @login_required
def member_dashboard(request):
    return render(request, "membersapp/dashboard.html")

# @login_required
def member_account(request):
    context = {
        "title": 'Business details'
    }
    return render(request, "")

# @login_required
def business_profile_edit(request):
    if request.method == 'POST':
        # Business images
        # password = request.FILES.get('password')
        print(request.POST)
        print(request.FILES)
        # # Business Data
        # password = request.POST.get('password')
        # business_name = request.POST.get('business_name')
        # business_address = request.POST.get('business_address')
        # business_about = request.POST.get('business_about')
        # business_services = request.POST.get('business_services')
        # business_phone = request.POST.get('business_phone')
        # business_email = request.POST.get('business_email')
        # business_wesite_url = request.POST.get('business_wesite_url')
        # business_facebook_url = request.POST.get('business_facebook_url')
        # business_linkedin_url = request.POST.get('business_linkedin_url')
        # business_twitter_url = request.POST.get('business_twitter_url')
        # business_whatsapp_url = request.POST.get('business_whatsapp_url')


    context = {
        "title": 'Business details'
    }
    return render(request, "membersapp/edit-profile.html", context)

# @login_required
def transaction_history(request):
    context = {
        "title": 'Transactions'
    }
    return render(request, "membersapp/under-construction.html", context)

# @login_required
def my_dues(request):
    return render(request, "membersapp/under-construction.html")

# @login_required
def member_logout(request):
    logout(request)
    messages.success(request, 'Logged out successfully')
    return redirect()