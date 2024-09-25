from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import *
from django.contrib.auth.models import  User
from mainapp.models import *
from django.db.utils import IntegrityError
import csv
import random
import string


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
    user_members = User.objects.filter(is_staff = False)
    '''
    # Search 
    if request.method == 'POST':
        search_word = request.POST.get('')
        members = Business.objects.filter(unit_name__icontains = search_word)

    else:
    '''

    context = {
        'members' : user_members,
        'units' : Unit.objects.all(),
        'admin' : current_admin,
        'businesses' : Business.objects.all(),
    }
    
    return render(request, "adminapp/admin-dashboard.html", context)

#@login_required
def admin_profile(request, id):
    # To handle login required
    if request.user.is_authenticated == False and request.user.is_staff == False:
        return redirect('admin-login')
    
    current_admin = User.objects.get(random_id = id)
    
    return render(request, "adminapp/under-construction.html")

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
                            first_name = '-----',
                            last_name = '-----',
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
                            random_id = random_id
                        )
            new_member.set_password('superadmin')
            
            new_member.save()
            new_member = User.objects.get(username = phone_number)
            new_business = Business(owner= new_member, 
                                    name = '-----',)
            new_business.save()
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
    # To handle login required
    if request.user.is_authenticated == False and request.user.is_staff == False:
        return redirect('admin-login')
    
    all_members = User.objects.filter(is_staff = False)
    for member in all_members:
        details =  [{'Business_name': member.first_name},
                    # {'Phone_number': member.phone_num},
                    # {'Email': member.email}, 
                    # {'Address': 'A Quiet Place'},
                    # {'Services': ''},
                    # {'Website': ''},
                    # {'Facebook': ''},
                    # {'Twitter(x)': ''},
                    # {'Linkedln': ''},
                    # {'Whatsapp': ''}
                    ]
    
    with open('members_list.csv', mode='w') as csvfile:
        for i in range(len(details)):
            fieldnames = details[i].keys()
            print(fieldnames)
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames, delimiter = ';')
        writer.writeheader()
        for row in details:
            writer.writerow(row)

    return redirect('manage-member')

#@login_required
def manage_member(request):
    # To handle login required
    if request.user.is_authenticated == False and request.user.is_staff == False:
        return redirect('admin-login')
    
    members = User.objects.filter(is_staff = False)
    businesses = Business.objects.all()

    context = {
        'members' : members,
        'businesses' : businesses,
    }
    return render(request, "adminapp/manage-membs.html",context)

#@login_required
def edit_member(request, id):
    # To handle login required
    if request.user.is_authenticated == False and request.user.is_staff == False:
        return redirect('admin-login')
    
    current_member = User.objects.get(random_id = id)
    
    member = User.objects.get(id = id)

    if request.method == 'POST':
        new_name = request.POST.get('')
        new_phone_no = request.POST.get('')
        new_email = request.POST.get('')

        #saving data to Business model
        member.name = new_name
        member.phone_no = new_phone_no
        member.email = new_email
        #Business.password = password

        Business.save()
        # the user model will be needed to save the passsword...
        pass
    return redirect("")

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

    return render(request, 'adminapp/pending-approvals.html')

#@login_required
def disapproved_profiles(request):
    # To handle login required
    if request.user.is_authenticated == False and request.user.is_staff == False:
        return redirect('admin-login')

    return render(request, 'adminapp/disapproved-profiles.html')

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