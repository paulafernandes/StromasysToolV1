from django.shortcuts import render
from django.http import HttpResponse
from .models import SystemTable

def index(request):
    context = {
        'systems': SystemTable.objects.all()
    }

    return render(request, 'tco_app/index.html', context)
    # return HttpResponse("Homepage")