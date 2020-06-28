from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User

class CreationUser(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','password1','password2']

class CheckOutForm(forms.Form):
    address1 = forms.CharField(widget=forms.TextInput(
                                attrs={
                                'class':'form-control'
                                }))
    address2 = forms.CharField(required=False,widget=forms.TextInput(
                                attrs={
                                'class':'form-control'
                                }))
    state = forms.CharField(widget=forms.TextInput(
                                attrs={
                                'class':'form-control'
                                }))
    zipcode = forms.IntegerField(widget=forms.TextInput(
                                attrs={
                                'class':'form-control'
                                }))
    phone = forms.IntegerField(widget=forms.TextInput(
                                attrs={
                                'class':'form-control'
                                }))
