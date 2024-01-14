from django import forms
from .models import ContactProfile  # importing the models that we made inside the models


class ContactForm(forms.ModelForm):
    name = forms.CharField(max_length=100, required=True,
        widget=forms.TextInput(attrs={
            'placeholder': '*Full name..',
            }))  # This will be rendered in HTML on the front-end
    email = forms.EmailField(max_length=254, required=True,
        widget=forms.TextInput(attrs={
            }))
    message = forms.CharField(max_length=1000, required=True,
        widget=forms.Textarea(attrs={
            'placeholder': '*Message..',
                                  'rows': 6,
                              }))

    class Meta:
        model = ContactProfile
        fields = ('name', 'email', 'message',)
