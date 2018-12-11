from django.shortcuts import render
from django.http import HttpResponse
from .models import SystemTable, ModelTable, LicenceTable, CpuTable
from django.core import serializers
import json
import sys
# from django.views.decorators.csrf import ensure_csrf_cookie

def index(request):
    context = {
        'systems': SystemTable.objects.all()
    }

    return render(request, 'tco_app/index.html', context)
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

# # @ensure_csrf_cookie
# # def all_json_models(request):
# def all_json_models(request, idsystem):
#     sys.stderr.write('teste')
#     if request.method == 'GET':
#         systemid = request.POST.get('id_system')
#         response_data = {}

#         models = ModelTable.objects.filter(id_system=idsystem)
#         # post = Post(text=post_text, author=request.user)
#         # post.save()

#         response_data['result'] = models
#         # response_data['postpk'] = post_text
#         # response_data['text'] = post.text
#         # response_data['created'] = post.created.strftime('%B %d, %Y %I:%M %p')
#         # response_data['author'] = post.author.username

#         return HttpResponse(
#             json.dumps(response_data),
#             content_type="application/json"
#         )
#         # return HttpResponse(
#         #     json.dumps(response_data),
#         #     content_type="application/json"
#         # )
#     else:
#         return HttpResponse(
#             json.dumps({"nothing to see": "this isn't happening"}),
#             content_type="application/json"
#         )
#         # return HttpResponse(
#         #     json.dumps({"nothing to see": "this isn't happening"}),
#         #     content_type="application/json"
#         # )