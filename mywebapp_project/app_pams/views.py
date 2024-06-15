from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def homepage(request):
  return HttpResponse("HomePage")

def newpatient(request):
  return HttpResponse("Add new patient Form")
