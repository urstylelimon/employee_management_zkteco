# employees/forms.py
from django import forms
from .models import Employee

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['name', 'rfid_card', 'job_description', 'expire_date']
        widgets = {
            'expire_date': forms.DateInput(attrs={'type': 'date'}),
        }
