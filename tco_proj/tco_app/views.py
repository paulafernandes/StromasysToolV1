from django.shortcuts import render
from django.http import HttpResponse
from .models import SystemTable, ModelTable, LicenceTable, CpuTable
from django.core import serializers
import json

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
    return render(request, "tco_app/simulation.html")

def all_json_models(request, system):
    if request.method == 'POST':
        post_text = request.POST.get('id_system')
        response_data = {}

        # post = Post(text=post_text, author=request.user)
        # post.save()

        response_data['result'] = 'Create post successful!'
        response_data['postpk'] = post_text
        # response_data['text'] = post.text
        # response_data['created'] = post.created.strftime('%B %d, %Y %I:%M %p')
        # response_data['author'] = post.author.username

        return HttpResponse(
            json.dumps(response_data),
            content_type="application/json"
        )
    else:
        return HttpResponse(
            json.dumps({"nothing to see": "this isn't happening"}),
            content_type="application/json"
        )