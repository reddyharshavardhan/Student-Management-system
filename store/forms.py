from django import forms
from .models import Branch

class BranchForm(forms.ModelForm):

    dob = forms.DateField(input_formats=['%Y-%m-%d'])

    class Meta:
        model = Branch

        fields = ['Reg', 'name', 'student_image', 'gender', 'dob', 'email', 'address', 'status']
        widgets = {
            'dob': forms.DateInput(attrs={'type': 'date'}),
        }
