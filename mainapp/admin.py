from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(User)
admin.site.register(Business)
admin.site.register(BusinessImages)
admin.site.register(Socials)
admin.site.register(Unit)
admin.site.register(Message)