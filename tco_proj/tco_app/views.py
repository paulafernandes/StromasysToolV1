from django.shortcuts import render
from django.http import HttpResponse
from .models import SystemTable, ModelTable, LicenceTable, CpuTable
from django.core import serializers
import json
import sys
import requests
import locale

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

def json_simulation(request, cpu, f_maintenance, currency):
    ####### Constants ##########
    f_power_instance = 150
    f_carbon_footprint = 0.744
    f_support = 467
    i_generic_power = 350
    ####### Constants ##########

    ######## DB QUERIES ##########
    f_licence = LicenceTable.objects.filter(cputable__id=cpu)[0].licence_cost
    f_power = ModelTable.objects.filter(cputable__id=cpu)[0].power_watt 

    f_power = float(f_power)
    f_power_instance = float(f_power_instance)
    f_carbon_power_legacy = float((f_power / 1000)*(24*365)) # Yearly power Consumption of the legacy system
    f_carbon_power_instance = float((f_power_instance / 1000)*(24*365)) # Yearly power Consumption of the instance
    f_carbon_footprint_legacy = (f_carbon_power_legacy * f_carbon_footprint) # Yearly carbon footprint of the legacy system
    f_carbon_footprint_instance = (f_carbon_power_instance * f_carbon_footprint) # Yearly carbon footprint of the instance
    f_carbon_footprint_savings = (f_carbon_footprint_legacy - f_carbon_footprint_instance) # Yearly carbon footprint savings
    f_power_savings = (f_carbon_power_legacy - f_carbon_power_instance)# Yearly Power Savings

    return HttpResponse(str(f_licence))
    #     # if currency == 'USD':
    #     base = "EUR"
    #     other = currency
    #     res = requests.get("http://data.fixer.io/api/latest?access_key=5b82db35be8ceb9321ca7a1502f1d704",
    #                     params={"base": base, "symbols": other})
    #     if res.status_code != 200:
    #         raise Exception("ERROR: API request unsuccessful.")
    #     data = res.json()
    #     rate = float(data["rates"][other])

    #     f_licence = f_licence * rate

    #     locale.setlocale(locale.LC_ALL, 'en-US.1252')
    #     f_total_savings = (f_maintenance - (f_licence + f_support))
    #     f_total_savings_currency = (locale.currency(f_total_savings,grouping=True))
    #     print('You could save',(f_total_savings_currency),', a reduction of',round((100-((f_licence*100)/f_maintenance))),'%')

    # sys.stderr.write('********************* : f_power= ' + str(f_power) + '\n')
    # sys.stderr.write('********************* : f_power_instance= ' + str(f_power_instance) + '\n')
    # sys.stderr.write('********************* : f_carbon_power_legacy= ' + str(f_carbon_power_legacy) + '\n')
    # sys.stderr.write('********************* : f_carbon_power_instance= ' + str(f_carbon_power_instance) + '\n')
    # sys.stderr.write('********************* : f_carbon_footprint_legacy= ' + str(f_carbon_footprint_legacy) + '\n')
    # sys.stderr.write('********************* : f_carbon_footprint_instance= ' + str(f_carbon_footprint_instance) + '\n')
    # sys.stderr.write('********************* : f_carbon_footprint_savings= ' + str(f_carbon_footprint_savings) + '\n')
    # sys.stderr.write('********************* : f_power_savings= ' + str(f_power_savings) + '\n')
    # import locale
    # locale.setlocale(locale.LC_ALL, 'pt-PT.1252')
    # f_total_savings = (f_maintenance - (f_licence + f_support))
    # f_total_savings_currency = (locale.currency(f_total_savings,grouping=True))

    # return HttpResponse('teste')