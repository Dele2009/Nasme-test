from django.shortcuts import render, redirect

# Create your views here.

def home_portal(request):

    return render(request, "mainapp/portal-home.html")

def business_details(request):

    return render(request, "mainapp/business-details.html")
