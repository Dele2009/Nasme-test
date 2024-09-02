from django.urls import path
from adminapp import views

urlpatterns = [
    path('admin-login', views.admin_login),
    path('admin-dashboard/',views.admin_home),
    path('admin-profile/', views.admin_account),
    path('register-admin/',views.register_admin),
    path('register-member/', views.register_member),
    path('manage-member', views.view_member),
    path('edit-member',views.edit_member),
    path('delete-member',views.delete_member),
    path('admin-logout', views.admin_logout),
]


