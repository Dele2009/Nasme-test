from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth import get_user_model

# Create your models here.


class User(AbstractUser):
    phone_num = models.PhoneNumberField()
    profile_pic = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=None)


 
