from django.shortcuts import render
from django.http import HttpResponse
from .models import SystemTable, ModelTable, LicenceTable, CpuTable
from django.core import serializers

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

def all_json_models(request, system):
    current_system = SystemTable.objects.all().filter(id=system)
    models = ModelTable.objects.all().filter(id_system_id=current_system)
    json_models = serializers.serialize("json", models)
    return HttpResponse(json_models, mimetype="aplication/javascript")