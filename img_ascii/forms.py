from django import forms
from .models import Images


class ImgUploadForm(forms.Form):
    image = forms.ImageField(allow_empty_file=False,label="")
    
    