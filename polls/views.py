from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def index(request):
    return HttpResponse("Python is awesome")



def pratik(request):
    return HttpResponse("ahgdvasbgdasghfdvas dasd ashdgasdgasjd asd jsahdjasdgjs ")


