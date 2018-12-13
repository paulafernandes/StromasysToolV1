from django.shortcuts import render
from django.http import HttpResponse
from .models import SystemTable, ModelTable, LicenceTable, CpuTable
from django.core import serializers
import json
import sys
# from django.views.decorators.csrf import ensure_csrf_cookie

def index(request):
    # context = {
    #     'systems': SystemTable.objects.all()
    # }

    return render(request, 'tco_app/index.html')
    # return HttpResponse("Homepage")

def modelsNames(request):
    context = {
        'models': ModelTable.objects.all()
    }

    return render(request, "tco_app/teste.html", context)

def system_choice(request):
    context = {
        'systems': SystemTable.objects.all()
    }
    return render(request, "tco_app/simulation.html", context)

def all_json_models(request, pk):
    # id_system = ModelTable.objects.get(id_system=systemid)
    models = ModelTable.objects.all().filter(id_system=pk)
    # sys.stderr.write('*********************: ' + 
    # str(ModelTable.objects.all().filter(id_system=systemid).count()))
    json_models = serializers.serialize('json', models)
    return HttpResponse(json_models, content_type='application/javascript')

def all_json_cpus(request, pk):
    # sys.stderr.write('*********************: ' + pk)
    cpus = CpuTable.objects.all().filter(id_model=pk)
    json_cpus = serializers.serialize('json', cpus)
    return HttpResponse(json_cpus, content_type='application/javascript')
