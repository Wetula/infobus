from django.http import HttpResponse
from django.shortcuts import render
from django.views import generic
from django.views.generic.base import TemplateView

from .models import Routes, Buses, Stops, Times


# Create your views here.

class HomePageView(TemplateView):
    template_name = 'base.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    def get(self, request, *args, **kwargs):
        return render(request, 'index.html')


def index(request):
    return HttpResponse("<h1>InfoBus Index<h1>")


def bus_route(request, bus_name):  # Przystanki linii
    bus_stop_list = Routes.objects.filter(busname=bus_name).order_by('stopnumber')
    context = {'bus_stop_list': bus_stop_list, 'bus_name': bus_name}
    return render(request, 'bus/index.html', context)


def bus_list(request):  # Lista linii
    buses_list = Buses.objects.order_by('busname')
    context = {'buses_list': buses_list}
    return render(request, 'buses/index.html', context)


class BusList(generic.ListView):
    model = Buses
    template_name = 'buslist/list.html'
    context_object_name = 'all_lines'

    def get_queryset(self):
        return Buses.objects.all()


def stop_info(request, stop_name):
    stop_id = Stops.objects.get(stopname=stop_name)
    buses = Times.objects.values('busname').distinct()
    timetable_list = Times.objects.filter(stopid=stop_id).values('busname', 'time')
    context = {'timetable_list': timetable_list, 'stop_name': stop_name, 'buses': buses}
    return render(request, 'stop/index.html', context)


def stop_list(request):
    stops_list = Stops.objects.order_by('stopname')
    context = {'stop_list': stops_list}
    return render(request, 'stops/index.html', context)


class StopList(generic.ListView):
    model = Stops
    template_name = 'stoplist/list.html'
    context_object_name = 'all_stops'

    def get_queryset(self):
        return Stops.objects.all()
