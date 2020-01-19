from .models import Buses, Stops


def bus_proc(request):
    lists = Buses.objects.values_list("busname", flat=True)
    return {'bus_list': lists}


def stop_proc(request):
    lists = Stops.objects.values_list('stopname', flat=True)
    return {'stop_list': lists}
