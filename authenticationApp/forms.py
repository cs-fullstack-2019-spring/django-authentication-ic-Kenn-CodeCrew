from django import forms
from .models import DMVModel

class DMVForm(forms.ModelForm):
    class Meta:
        model = DMVModel
        exclude = ["userTableForeignKey"]
