from django.shortcuts import render
from .models import Patient
from .forms import Patient
# Create your views here.


def patient(request):
        if request.method == 'POST':
            form = Patient(request.POST)
            if form.is_valid():
               form.save()
        else:
            form=Patient()
        return render(request, "book.html", { 'form' : form } )