from django import forms
from django.forms import ModelForm
from .models import Student

class StudentForm(ModelForm):

    class Meta:
        model = Student
        fields = ['name', 'age', 'email']

    #Field-level validation
    def clean_age(self):
        age = self.cleaned_data.get('age')
        if age < 18:
            raise forms.ValidationError("Age must be at least 18.")
        return age
    
    #Form-level validation
    def clean(self):
        cleaned_data = super().clean()
        name = cleaned_data.get('name')
        email = cleaned_data.get('email')

        if email and email.endswith('@example.com'):
            raise forms.ValidationError("Email cannot be from example.com domain.")
        return cleaned_data
           
            