from django.shortcuts import render
from django.http import HttpResponse
from .models import SystemTable, ModelTable, LicenceTable, CpuTable

def index(request):
    context = {
        'systems': SystemTable.objects.all()
    }

    return render(request, 'tco_app/simulation.html', context)
    # return HttpResponse("Homepage")

def modelsNames(request):
    context = {
        'models': ModelTable.objects.all()
    }

    return render(request, "tco_app/teste.html", context)