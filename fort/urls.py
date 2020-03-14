from django.urls import path
from . import views


urlpatterns = [
    path('', views.index),
    path('upcoming', views.upcoming),
    path('global_stats', views.global_stats),
    path('stats', views.stats),
    path('news', views.news),
    path('find_id', views.find_id),
    path('your_id', views.your_id),
    path('weapon_detail', views.weapon_detail),
    path('events', views.events),
]
