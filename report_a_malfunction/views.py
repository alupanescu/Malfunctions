from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader

from .models import Malfunction


# Create your views here.
def index(request):
    context = {
        'segment':'index',
        'malfunctions':Malfunction.objects.all()
               }
    template=loader.get_template("report_a_malfunction/index.html")
    return HttpResponse(template.render(context, request))