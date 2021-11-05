from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    #return HttpResponse("Hello")
    return render(request,'html/index.html',{'home':'Han'})
# Create your views here.

