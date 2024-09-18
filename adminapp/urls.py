from django.urls import path
from adminapp import views

urlpatterns = [
    path('admin-login', views.admin_login, name='admin-login'),
    path('admin-dashboard/',views.admin_dashboard, name='admin-dashboard'),
    path('admin-profile/', views.admin_profile, name='admin-profile'),
    path('manage-admin/', views.manage_admin, name='manage-admin'),
    path('register-admin/',views.register_admin, name='register-admin'),
    path('register-member/', views.register_member, name='register-member'),
    path('bulk-register/', views.bulk_register,name='bulk-register'),
    path('manage-member/', views.manage_member, name='manage-member'),
    path('edit-member/',views.edit_member, name='edit-member'),
    path('delete-member/',views.delete_member, name='delete-member'),
    path('manage-unit/', views.manage_unit, name='manage-unit'),
    path('edit-unit/', views.edit_unit, name='edit-unit'),
    path('add-unit/', views.add_unit, name='add-unit'),
    path('delete-unit/', views.delete_unit, name='delete-unit'),
    path('approvals/', views.approvals, name='approvals'),
    path('unit-message/', views.unit_message, name='unit-message'),
    path('admin-logout/', views.admin_logout, name='admin-logout'),
]
