from django.urls import path
from membersapp import views

urlpatterns = [
     path('', views.member_dashboard, name='dashboard'),
     path('edit-profile/', views.business_profile_edit, name='edit-profile'),
     path('my-dues/', views.my_dues, name='my-dues'),
     path('transaction-log/', views.transaction_history, name='transaction-log'),
     path('member-logout/', views.member_logout, name='member-logout'),
]
