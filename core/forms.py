from django import forms 

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Your Name'}))
    email = forms.EmailField(widget=forms.TextInput(attrs={'placeholder': 'Your Email'}))
    message = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Your Message'}))
