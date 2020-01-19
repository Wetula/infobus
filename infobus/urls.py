from django.urls import path

from infobus.views import HomePageView
from . import views

urlpatterns = [
    # ex: /infobus/
    path('', HomePageView.as_view(), name='base'),
    # path('', views.index, name='base'),
    # ex /bus/100
    path('bus/<int:bus_name>/', views.bus_route, name='bus_route'),
    # ex /buses
    path('buses', views.bus_list),
    # ex /stops
    path('stops', views.stop_list),
    # ex /stop/Arkady
    path('stop/<str:stop_name>', views.stop_info, name='stop_times')
]
