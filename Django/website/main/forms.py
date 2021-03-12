from django import forms

class CreateNewList(forms.Form):
    name = forms.CharField(label="Name of list", max_length=200)
    check = forms.BooleanField(label="Check", required=False)
