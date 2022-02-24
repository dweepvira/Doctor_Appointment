from django import forms
from .models import Patient

class Patient(forms.ModelForm):
    class Meta:
        model=Patient
        fields=[
            'patient_name',
            'patient_age',
            'patient_problem',
            'time',
        ]