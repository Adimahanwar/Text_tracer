from django import forms

class HandwrittenImageForm(forms.Form):
    image = forms.ImageField()
