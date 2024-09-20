from django.urls import path
from adminapp import views

urlpatterns = [
    path('admin-login/', views.admin_login, name='admin-login'),
    path('',views.admin_dashboard, name='admin-dashboard'),
    path('admin-profile/', views.admin_profile, name='admin-profile'),
    path('manage-admin/', views.manage_admin, name='manage-admin'),
    path('register-admin/',views.register_admin, name='register-admin'),
    path('register-member/', views.register_member, name='register-member'),
    path('bulk-register/', views.bulk_register,name='bulk-register'),
    path('manage-member/', views.manage_member, name='manage-member'),
    path('edit-member/',views.edit_member, name='edit-member'),
    path('delete-member/',views.delete_member, name='delete-member'),
    path('manage-unit/', views.manage_unit, name='manage-unit'),
    path('add-unit/', views.add_unit, name='add-unit'),
    path('delete-unit/', views.delete_unit, name='delete-unit'),
    path('pending-approvals/', views.pending_approvals, name='pending-approvals'),
    path('disapproved-profiles/', views.disapproved_profiles, name='disapproved-profiles'),
    path('unit-message/', views.unit_message, name='unit-message'),
    path('create-payment/', views.create_payment, name='create-payment'),
    path('financial-report/', views.financial_report, name='financial-report'),
    path('under-construction/', views.under_construction, name='under-construction'),
    path('export-members/', views.export_members, name='export-members'),
    path('admin-logout/', views.admin_logout, name='admin-logout'),
]
