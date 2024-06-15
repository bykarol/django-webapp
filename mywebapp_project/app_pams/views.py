from django.shortcuts import render
from . forms import PatientForm

# Create your views here.
def homepage(request):
    return render(request, "homepage.html")

def newpatient(request):
  if request.method == 'POST':
     form = PatientForm(request.POST)
     if form.is_valid():
        form.save()
  else:
     form = PatientForm()
  return render(request, "patientform.html", {'form': form})
