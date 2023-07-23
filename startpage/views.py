from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
# Create your views here.
def index(request):
    template = loader.get_template("startpage/base.html")
    return HttpResponse(template.render({}, request))

def home(request):
    template = loader.get_template("startpage/home.html")
    return HttpResponse(template.render({}, request))

def about(request):
    template = loader.get_template("startpage/about.html")
    return HttpResponse(template.render({}, request))