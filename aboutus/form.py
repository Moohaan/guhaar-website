from django import forms

class ContactusForm(forms.Form):
    name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Username'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control','placeholder':'Email'}))
    message = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control','placeholder':'Type your Message'}))
