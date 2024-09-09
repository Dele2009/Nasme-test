from django.urls import path
from adminapp import views

urlpatterns = [
    path('admin-login', views.admin_login),
    path('admin-dashboard/',views.admin_home),
    path('admin-profile/', views.admin_profile),
    path('manage-admin', views.manage_admin),
    path('register-admin/',views.register_admin),
    path('register-member/', views.register_member),
    path('bulk-register', views.bulk_register),
    path('manage-member', views.manage_member),
    path('edit-member',views.edit_member),
    path('delete-member',views.delete_member),
    path('manage-unit', views.manage_unit),
    path('edit-unit', views.edit_unit),
    path('add-unit', views.add_unit),
    path('delete-unit', views.delete_unit),
    path('approvals', views.approvals),
    path('unit-message', views.unit_message),
    path('admin-logout', views.admin_logout),
]
