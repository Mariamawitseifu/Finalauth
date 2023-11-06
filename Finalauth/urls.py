from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api1/', include('announce.urls')),  # Include the app's URLs
     path('api/', include('records.urls')),
]