from django import forms


class SubscribeForm(forms.Form):
    fullname = forms.CharField(label='Your Full Name', max_length=100, min_length=5)
    email = forms.EmailField(label='Your Email', max_length=100)
