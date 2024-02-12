from django import forms

class UpdateItemForm(forms.Form):
    description = forms.Textarea(max_length=1024*8)
    price = forms.IntegerField()

