
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

# Import the custom 404 view
from .views import custom_404 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('mainapp.urls')),
    path('testadmin/', include('adminapp.urls')),
    path('member/', include('membersapp.urls')),
]
# Configure the custom 404 handler
handler404 = 'NasmeDjango.views.custom_404'
urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)