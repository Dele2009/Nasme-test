from django.urls import path
from . import views
#from mainapp.urls import views

urlpatterns = [
    path('',views.home_portal,name='home'),
    path('business-details',views.business_details,name='business-details'),

]
