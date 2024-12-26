# from django import forms
# from .models import Prescription

# class PrescriptionUploadForm(forms.ModelForm):
#     class Meta:
#         model = Prescription
#         fields = ['file']

import os
from django import forms
from .models import Prescription

class PrescriptionUploadForm(forms.ModelForm):
    class Meta:
        model = Prescription
        fields = ['file']
    
    def clean_file(self):
        file = self.cleaned_data.get('file')
        if file:
            # Extract file extension
            file_extension = os.path.splitext(file.name)[1].lower()
            allowed_extensions = ['.pdf', '.png', '.jpg', '.jpeg']
            
            # Check if the file extension is allowed
            if file_extension not in allowed_extensions:
                raise forms.ValidationError('Choose a .pdf, .png, .jpg, or .jpeg file.')

        return file
