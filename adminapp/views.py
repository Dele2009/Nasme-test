from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import *
from django.contrib.auth.models import  User
from mainapp.models import *

# Create your views here.
def admin_login(request):

    #Login form
    if request.method == 'POST':
        email = request.POST.get('')
        password = request.POST.get('')

        admin_auth = authenticate(email=email, password=password)

        if admin_auth is not None:
            login(request, admin_auth)
            return redirect('admin-dashboard')
        else:
            return redirect(request,'admin-login')
    return render(request, "adminapp/admin_login.html")

#@login_required
def admin_dashboard(request):
    '''
    members = Business.objects.all()
    current_admin = User.objects.get(username = request.user)

    # Search 
    if request.method == 'POST':
        search_word = request.POST.get('')
        members = Business.objects.filter(unit_name__icontains = search_word)

    else:
        members = Business.objects.all()

    context = {
        'members' : members,
        'units' : Unit.objects.all(),
    }
    '''
    return render(request, "adminapp/admin-dashboard.html")

#@login_required
def admin_profile(request):
    return render(request, "")

# @login_required
def manage_admin(request):

    return render(request, 'adminapp/manage-admin.html')

#@login_required
def register_admin(request):

    if request.method == 'POST':
        pass
    return render(request, "adminapp/add-admin.html")

#@login_required
def register_member(request):

    if request.method == 'POST':
        #getting the data
        business_name = request.POST.get('')
        phone_no = request.POST.get('')
        email = request.POST.get('')
        unit = request.POST.get('')
        address = request.POST.get('')
        services = request.POST.get('')
        about = request.POST.get('')
        logo = request.POST.get('')
        business_images = request.POST.get('')
        website = request.POST.get('')
        facebook = request.POST.get('')
        twitter = request.POST.get('')
        linkedln = request.POST.get('')
        whatsapp = request.POST.get('')

        #savng data to Business model
        Business.owner = ''
        Business.name = business_name
        Business.email = email
        Business.phone_no = phone_no
        Business.address = address
        Business.services = services
        Business.about = about
        Business.logo = logo

        #saving to BusinessImages model
        BusinessImages.image = business_images

        #saving to Socials model
        Socials.website = website
        Socials.facebook = facebook
        Socials.whatsapp = whatsapp
        Socials.linkedin = linkedln
        Socials.twitter = twitter

        Business.save()
        BusinessImages.save()
        Socials.save()
        pass

    return render(request, "adminapp/add-member.html")

#@login_required
def bulk_register(request):
    return render(request, 'adminapp/bulk-reg.html')

#@login_required
def manage_member(request):
    members = Business.objects.all()

    context = {
        'all_members' : members,
    }
    return render(request, "adminapp/manage-membs.html",context)

#@login_required
def edit_member(request, id):
    member = Business.objects.get(id = id)

    if request.method == 'POST':
        name = request.POST.get('')
        phone_no = request.POST.get('')
        email = request.POST.get('')
        password = request.POST.get('')

        #saving data to Business model
        Business.name = name
        Business.phone_no = phone_no
        Business.email = email
        #Business.password = password

        Business.save()
        # the user model will be needed to save the passsword...
        pass
    return render(request, "")

#@login_required
def delete_member(request, id):
    member = Business.objects.get(id = id)
    member.delete()

    return render(request, "")

#@login_required
def manage_unit(request):
    units = Unit.objects.all()
    return render(request,'')

#@login_required
def edit_unit(request):

    return render(request,'')

#@login_required
def add_unit(request,):
    if request.method == 'POST':
        unit = request.POST.get('')

        new_unit = Unit(name = unit)
        new_unit.save()
    else:
        pass
    return render(request,'adminapp/add-unit.html')

#@login_required
def delete_unit(request):
    return render(request,'')

#@login_required
def approvals(request):

    return render(request, '')

#@login_required
def unit_message(request):

    return render(request, 'adminapp/send-message.html')

#@login_required
def admin_logout(request):
    logout(request)
    return redirect('admin-login')