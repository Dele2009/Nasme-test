from django.urls import path
from membersapp import views

urlpatterns = [
     path('member-login/', views.member_login, name='member-login'),
     path('', views.member_dashboard, name='member-dashboard'),
     path('edit-profile/<str:id>/', views.business_profile_edit, name='edit-member-profile'),
     path('messages/', views.get_messages_or_alerts, name='messages'),
     path('my-dues/', views.my_dues, name='my-dues'),
     path('transaction-log/', views.transaction_history, name='transaction-log'),
     path('member-logout/', views.member_logout, name='member-logout'),
]
