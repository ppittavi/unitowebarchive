from django.shortcuts import render
from django.template import loader
from site_archives.models import Archive

# Create your views here.
from django.http import HttpResponse

def index(request):
    template = loader.get_template('index.html')
    data = Archive.objects.all().filter(archive_online=True)
    context = {
            'items': data,
    }
    return HttpResponse(template.render(context, request))



def summary(request):
    template = loader.get_template('summary.html')
    data = Archive.objects.all().filter(archive_online=True)
    context = {
            'items': data,
    }
    return HttpResponse(template.render(context, request))
