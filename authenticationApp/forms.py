from django import forms
from .models import DMVModel, BankAccountModel

class DMVForm(forms.ModelForm):
    class Meta:
        model = DMVModel
        exclude = ["userTableForeignKey"]
        # fields = ["IDNumber", "stateAbbr", "issueDate"]


class BankAccountForm(forms.ModelForm):
    class Meta:
        model = BankAccountModel
        exclude = ["linkUserForeignKey"]
