from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import  User
from mainapp.models import *
from PIL import Image
from io import BytesIO
from django.core.files.base import ContentFile

# Create your views here.

def member_login(request):
    match request.user:
        case _ if request.user.is_authenticated == True:
            return redirect('member-dashboard')
        case _ if request.user.is_staff == True:
            return redirect('member-dashboard')
    #Login form
    if request.method == 'POST':
        phone_num = request.POST.get('phone_num')
        password = request.POST.get('password')
        
        member_auth = authenticate(username=phone_num, password=password)
        if member_auth is not None:
            login(request, member_auth)
            if request.user.is_staff == False:
                return redirect('member-dashboard')
            else:
                return redirect('member-login')
        else:
            return redirect('member-login')
    return render(request, "membersapp/member_login.html")

# @login_required
def member_dashboard(request):
    match request.user:
        case _ if request.user.is_authenticated == False:
            return redirect('member-login')
        case _ if request.user.is_staff == True:
            return redirect('member-login')
    current_member = User.objects.get(username = request.user)

    context = {
        'member' : current_member,
    }
    return render(request, "membersapp/dashboard.html", context)

# @login_required
def member_account(request):
    match request.user:
        case _ if request.user.is_authenticated == False:
            return redirect('member-login')
        case _ if request.user.is_staff == True:
            return redirect('member-login')
         
    context = {

    }
    return render(request, "")

# @login_required
def business_profile_edit(request,id):
    match request.user:
        case _ if request.user.is_authenticated == False:
            return redirect('member-login')
        case _ if request.user.is_staff == True:
            return redirect('member-login')
         
    current_member = User.objects.get(random_id = id)
    if current_member.business:
            business = Business.objects.get(owner = current_member)
    else:
        business = Business(owner = current_member)
        business.save()
        business = Business.objects.get(owner = current_member)

    if business.socials:
        socials = Socials.objects.get(owner = business)
    else:
        socials = Socials(owner = business)
        socials.save()
        socials = Socials.objects.get(owner = business)

    if business.businessimages_set.exists():
        business_images = BusinessImages.objects.filter(owner=business)
    else:
        business_images = BusinessImages(owner=business)
        business_images.save()
        business_images = BusinessImages.objects.get(owner = business)

    images = []
    for image in business_images:
        images.append(image.image.url)

    if request.method == 'POST':
        image_file = request.FILES.get('business_photo')
        business_name = request.POST.get('business_name')
        business_address = request.POST.get('business_address')
        business_about = request.POST.get('business_about')
        business_services = request.POST.get('business_services')
        business_phone_num = request.POST.get('business_phone')
        business_email = request.POST.get('business_email')
        business_website = request.POST.get('business_website_url')
        business_facebook = request.POST.get('business_facebook_url')
        business_linkedln = request.POST.get('business_linkedin_url')
        business_twitter = request.POST.get('business_twitter_url')
        business_whatsapp = request.POST.get('business_whatsapp_url')

    
        if image_file:
            img = Image.open(image_file)
            img = img.resize((1024, 1024), Image.Resampling.LANCZOS)
            if img.mode == 'RGBA':
                # Convert the image to RGB before saving as JPEG
                img = img.convert('RGB')
            img_io = BytesIO()
            img.save(img_io, format='JPEG')
            img_content = ContentFile(img_io.getvalue(), name=image_file.name)
            current_member.profile_pic.delete()
            current_member.profile_pic = img_content
        
        business.name = business_name
        business.address = business_address
        business.about = business_about
        business.services = business_services
        business.phone_num = business_phone_num
        business.email = business_email
        socials.website = business_website
        socials.facebook = business_facebook
        socials.linkedln = business_linkedln
        socials.twitter = business_twitter
        socials.whatsapp = business_whatsapp
        
        current_member.save()
        business.save()
        socials.save()


    context = {
        "member": current_member,
        "business" : business,
        "socials" : socials,
        "business_images" : images,
    }
    return render(request, "membersapp/edit-profile.html", context)

# @login_required
def transaction_history(request):
    match request.user:
        case _ if request.user.is_authenticated == False:
            return redirect('member-login')
        case _ if request.user.is_staff == True:
            return redirect('member-login')
    context = {

    }
    return render(request, "membersapp/under-construction.html", context)

# @login_required
def my_dues(request):
    match request.user:
        case _ if request.user.is_authenticated == False:
            return redirect('member-login')
        case _ if request.user.is_staff == True:
            return redirect('member-login')
    return render(request, "membersapp/under-construction.html")

# @login_required
def member_logout(request):
    logout(request)
    messages.success(request, 'Logged out successfully')
    return redirect('member-login')