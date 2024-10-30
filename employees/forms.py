# employees/forms.py
from django import forms
from .models import Employee

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['name', 'rfid_card', 'job_description', 'road_number', 'house_number', 'expire_date']
        widgets = {
            'expire_date': forms.DateInput(attrs={'type': 'date','class': 'custom-input'}),
            'name': forms.TextInput(attrs={'placeholder': 'Enter employee name'}),
            'job_description': forms.TextInput(attrs={'placeholder': 'Enter job description'}),
            'house_number': forms.TextInput(attrs={'placeholder': 'Enter house number'}),
            'rfid_card': forms.NumberInput(attrs={'placeholder': 'Enter RFID number'}),
        }
