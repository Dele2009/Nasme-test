from django.shortcuts import render, redirect
from .models import Business, User, BusinessImages, Socials

# Create your views here.

def home_portal(request):
    businesses = Business.objects.all()
    businesses = businesses.filter(owner__is_active =True)
    search_query = request.GET.get('member_search')

    if search_query:
        try:
            search_query = int(search_query)
            businesses = businesses.filter(phone_num__contains = search_query)
        except ValueError:
            search_query = request.GET.get('member_search')

            if '.com' in search_query:
                businesses = businesses.filter(email__contains = search_query)
            else:
                businesses = businesses.filter(name__contains = search_query)
    context = {
        'businesses' : businesses.reverse(),
    }
    return render(request, "mainapp/portal-home.html", context)

def business_details(request, id):
    business_owner = User.objects.get(random_id = id)
    business = Business.objects.get(owner = business_owner)
    business_images = BusinessImages.objects.filter(owner = business)
    socials = Socials.objects.get(owner = business)

    context = {
        'user' : business_owner,
        'business' : business,
        'business_images' : business_images,
        'socials' : socials,
    }

    return render(request, "mainapp/business-details.html", context)
