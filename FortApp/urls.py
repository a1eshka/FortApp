from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('fort.urls')),
    path('upcoming', include('fort.urls')),
    path('global_stats', include('fort.urls')),
    path('stats', include('fort.urls')),
    path('news', include('fort.urls')),
    path('find_id', include('fort.urls')),
    path('your_id', include('fort.urls')),
    path('weapon_detail', include('fort.urls')),
    path('events', include('fort.urls')),
]
