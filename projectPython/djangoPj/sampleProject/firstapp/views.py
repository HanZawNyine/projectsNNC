from django.shortcuts import render
from  django.http import HttpResponse

# Create your views here.
def home(requet):
    return HttpResponse("Hello Home")