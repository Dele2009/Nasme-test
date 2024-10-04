from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import *
from django.urls import reverse
# from django.contrib.auth.models import  User
from django.contrib.auth import get_user_model
from mainapp.models import *
from django.db.utils import IntegrityError
import csv
import random
import string
from PIL import Image
from django.core.files.base import ContentFile
from io import BytesIO


User = get_user_model()


def generate_random_string():
    chars = string.ascii_letters + string.digits  # Upper and lowercase letters + digits
    sections = [''.join(random.choices(chars, k=5)) for _ in range(4)]  # Generate 4 sections of 5 characters
    return '-'.join(sections)


# Create your views here.
def admin_login(request):
    # If user is already logged in
    if request.user.is_authenticated == True and request.user.is_staff == True:
        messages.warning(request, 'User is already logged in...')
        return redirect('/')
    

    #Login form
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        admin_auth = authenticate(username=email, password=password)

        if admin_auth is not None:
            login(request, admin_auth)
            if request.user.is_staff == True:
                return redirect('admin-dashboard')
            else:
                return redirect('admin-login')
        else:
            return redirect('admin-login')
    return render(request, "adminapp/admin_login.html")

#@login_required
def admin_dashboard(request):
    # To handle login required
    if request.user.is_authenticated == False and request.user.is_staff == False:
        return redirect('admin-login')

    current_admin = User.objects.get(username = request.user)
    active_users = User.objects.all()
    active_members = active_users.filter(is_active = True)
    active_members = active_members.filter(is_staff = False)

    '''
    # Search 
    if request.method == 'POST':
        search_word = request.POST.get('')
        members = Business.objects.filter(unit_name__icontains = search_word)

    else:
    '''

    context = {
        'active_users' : active_users,
        'active_members': active_members,
        'units' : Unit.objects.all(),
        'admin' : current_admin,
        'businesses' : Business.objects.all(),
    }
    
    return render(request, "adminapp/admin-dashboard.html", context)

#@login_required
def admin_profile(request):
    # To handle login required
    if request.user.is_authenticated == False and request.user.is_staff == False:
        return redirect('admin-login')
    
    if request.method == 'POST':
        image = request.FILES.get('file')
        
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        phone = request.POST.get('phone')
        email = request.POST.get('email')

        user = get_object_or_404(User, id = request.user.id)
        if image and not user.profile_pic:
            user.profile_pic = image
        user.first_name = fname
        user.last_name = lname
        user.phone_num = phone
        user.email = email
        user.save()
        
        messages.success(request, message='Your profile has been updated successfully.')
        return redirect(request.path)
        

    current_admin = request.user
    context = {
        'current_admin': current_admin
    }
    return render(request, "adminapp/admin-profile.html", context)

# @login_required
def manage_admin(request):
    # To handle login required
    if request.user.is_authenticated == False and request.user.is_staff == False:
        return redirect('admin-login')

    all_admins = User.objects.filter(is_staff = True)
    context = {
        'admins' : all_admins
    }
    return render(request, 'adminapp/manage-admin.html', context)

#@login_required
def register_admin(request):
    # To handle login required
    if request.user.is_authenticated == False and request.user.is_staff == False:
        return redirect('admin-login')

    try:
        if request.method == 'POST':
            email = request.POST.get('email')
            random_id = generate_random_string()
            new_admin = User.objects.create(
                            # first_name = '-----',
                            # last_name = '-----',
                            username = email,
                            email = email,
                            random_id = random_id
                        )
            new_admin.set_password('superadmin')
            new_admin.is_staff = True
            if 'is_superadmin' in request.POST:
                new_admin.is_superuser = True
                new_admin.save()
            else:
                new_admin.save()
            messages.success(request, 'New admin successfully added.')
            return redirect(reverse('manage-admin'))
    except IntegrityError:
            messages.error(request, 'Email already exists')
    return render(request, "adminapp/add-admin.html")

#@login_required
def register_member(request):
    # To handle login required
    if request.user.is_authenticated == False and request.user.is_staff == False:
        return redirect('admin-login')
    members = len(User.objects.filter(is_staff = False))

    if request.method == 'POST':
        try:
            random_id = generate_random_string()
            phone_number = request.POST.get('phoneNumber')
            new_member = User.objects.create(
                            first_name = '-----',
                            last_name = '-----',
                            username = phone_number,
                            email = '-----',
                            phone_num = phone_number,
                            random_id = random_id,
                            is_active = False
                        )
            new_member.set_password('12345678')
            
            new_member.save()
            # new_member = User.objects.get(username = phone_number)
            # new_business = Business(owner= new_member, 
            #                         name = '-----',)
            # new_business.save()
        except IntegrityError:
            messages.error(request, 'Phone number already exists')

    return render(request, "adminapp/add-member.html")

#@login_required
def bulk_register(request):
    # To handle login required
    if request.user.is_authenticated == False and request.user.is_staff == False:
        return redirect('admin-login')
    
    return render(request, 'adminapp/bulk-reg.html')

def export_members(request):
    import csv
from django.http import HttpResponse
from django.shortcuts import redirect

def export_members(request):
    # Handle login required
    if not request.user.is_authenticated or not request.user.is_staff:
        return redirect('admin-login')
    
    # Create the HttpResponse object with CSV headers
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="members_list.csv"'

    writer = csv.writer(response)
    # Writing the header row
    writer.writerow(['Business Name', 'Phone Number', 'Email', 'Address', 'Services', 'Website', 'Facebook', 'Twitter (X)', 'LinkedIn', 'WhatsApp'])

    # Fetch all non-staff users
    all_members = User.objects.filter(is_staff=False)
    all_members = all_members.filter(is_active = True)
    
    # Loop through each user and extract their details along with business details
    for member in all_members:
        current_member = member.username
        print(current_member)
        business = Business.objects.get(owner = current_member)
        print(business)

        writer.writerow([
            business.name,
            member.phone_num,
            member.email,
            business.address,
            business.services,
            'N/A',
            'N/A',
            'N/A',
            'N/A',
            'N/A',

        ])

    #return response

    return redirect('manage-member'), response

#@login_required
def manage_member(request):
    # To handle login required
    if request.user.is_authenticated == False and request.user.is_staff == False:
        return redirect('admin-login')
    
    if request.method == 'POST':
        member_id = request.POST.get('member_id')
        current_member = User.objects.get(random_id = member_id)
        
        member_business = Business.objects.get(owner = current_member.id)
        
        if 'save_edit' in request.POST:

            new_name = request.POST.get('business_name')
            new_number = request.POST.get('phone_num')
            new_email = request.POST.get('email')
            image_file = request.FILES.get('business_image')
            print(image_file)

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

            member_business.name = new_name
            current_member.phone_num = new_number
            current_member.username = new_number
            current_member.email = new_email
            member_business.save()
            current_member.save()
        
        elif 'delete_member' in request.POST:
            member_id = request.POST.get('member_id')
            member = User.objects.get(random_id = member_id)
            member.profile_pic.delete()
            member.delete()
        
        elif 'suspend_member' in request.POST:
            member_id = request.POST.get('member_id')
            suspend_message = request.POST.get('suspend_message')

            member = User.objects.get(random_id = member_id)
            member.suspend_message = suspend_message
            member.is_active = False
            member.is_suspended = True
            member.save()

        elif 'submit_member_message' in request.POST:
            member_id = request.POST.get('member_id')
            member_message = request.POST.get('member_message')

            member = User.objects.get(random_id = member_id)

            message = Message(owner = member, 
                              message = member_message)
            message.save()
            
    members = User.objects.filter(is_staff = False)
    members = members.filter(is_active = True)
    businesses = Business.objects.filter(owner__is_active = True)

    context = {
        'members' : members,
        'businesses' : businesses,
    }
    return render(request, "adminapp/manage-membs.html",context)


#@login_required
def delete_member(request, id):
    # To handle login required
    if request.user.is_authenticated == False and request.user.is_staff == False:
        return redirect('admin-login')
    
    current_member = User.objects.get(random_id = id)
    current_member.delete()

    return redirect(request, "manage-member")

#@login_required
def manage_unit(request):
    # To handle login required
    if request.user.is_authenticated == False and request.user.is_staff == False:
        return redirect('admin-login')
    
    units = Unit.objects.all()
    if request.method == 'POST':
        unit_id = request.POST.get('unit-id')
        new_unit_name = request.POST.get('unit-name')

        unit = Unit.objects.get(id = unit_id)
        unit.unit_name = new_unit_name
        unit.save()

        return redirect('manage-unit')

    context = {
        'units' : units,
    }

    return render(request,'adminapp/manage-unit.html', context)

#@login_required
def add_unit(request,):
    # To handle login required
    if request.user.is_authenticated == False and request.user.is_staff == False:
        return redirect('admin-login')
    
    if request.method == 'POST':
        unit = request.POST.get('unit_name')
        if unit is not None and len(unit.strip()) > 5:
            new_unit = Unit(unit_name = unit)
            new_unit.save()
            messages.success(request, 'Unit created successfully')
        else:
            messages.warning(request, 'Invalid input, Length of unit name should be greater than 5 chahracters')
    return render(request,'adminapp/add-unit.html')

#@login_required
def delete_unit(request, id):
    # To handle login required
    if request.user.is_authenticated == False and request.user.is_staff == False:
        return redirect('admin-login')
    
    unit = Unit.objects.get(id = id)
    unit.delete()
    
    return render(request,'')

#@login_required
def pending_approvals(request):
    # To handle login required
    if request.user.is_authenticated == False and request.user.is_staff == False:
        return redirect('admin-login')

    users = User.objects.filter(is_active = False)
    users = users.filter(is_suspended = False)
    businesses = Business.objects.all()

    context = {
        'users' : users,
        'businesses' : businesses,
    }

    return render(request, 'adminapp/pending-approvals.html', context)

#@login_required
def disapproved_profiles(request):
    # To handle login required
    if request.user.is_authenticated == False and request.user.is_staff == False:
        return redirect('admin-login')
    
    users = User.objects.filter(is_suspended = True)
    businesses = Business.objects.all()

    context = {
        'users' : users,
        'businesses' : businesses,
    }


    return render(request, 'adminapp/disapproved-profiles.html', context)

#@login_required
def approved_profiles(request):
    # To handle login required
    if request.user.is_authenticated == False and request.user.is_staff == False:
        return redirect('admin-login')

    return render(request, 'adminapp/approved-profiles.html')

#@login_required
def unit_message(request):
    # To handle login required
    if request.user.is_authenticated == False and request.user.is_staff == False:
        return redirect('admin-login')
    
    # To send message to a unit
    if request.method == 'POST':

        # To send message to all units
        if 'sendAll' in request.POST:
            pass

        else:
            pass

    context = {
        'units' : Unit.objects.all()
    }
    return render(request, 'adminapp/send-message.html', context)

#@login_required
def create_payment(request):
    # To handle login required
    if request.user.is_authenticated == False and request.user.is_staff == False:
        return redirect('admin-login')
    
    return render(request, 'adminapp/under-construction.html')

#@login_required
def financial_report(request):
    # To handle login required
    if request.user.is_authenticated == False and request.user.is_staff == False:
        return redirect('admin-login')
    
    return render(request, 'adminapp/under-construction.html')

#@login_required
def under_construction(request):
    # To handle login required
    if request.user.is_authenticated == False and request.user.is_staff == False:
        return redirect('admin-login')
    
    return render(request, 'adminapp/under-construction.html')

#@login_required
def admin_logout(request):
    # To handle login required
    if request.user.is_authenticated == False and request.user.is_staff == False:
        return redirect('admin-login')
    
    logout(request)
    return redirect('admin-login')