from django import forms
from django.contrib.auth.models import User


class userregform(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']

class userlogform(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(max_length=20)

class sellerregform(forms.Form):
    companyname = forms.CharField(max_length=25)
    email = forms.EmailField()
    password = forms.CharField(max_length=20)
    cpassword = forms.CharField(max_length=20)
    number = forms.IntegerField()
    address = forms.CharField(max_length=100)

class sellerlogform(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(max_length=20)

class addproductform(forms.Form):
    image = forms.ImageField()
    pname = forms.CharField(max_length=25)
    price = forms.IntegerField()

class paymentform(forms.Form):
    pname = forms.CharField(max_length=50)
    price = forms.CharField(max_length=20)
    fname = forms.CharField(max_length=20)
    address = forms.CharField(max_length=50)
    email = forms.EmailField()
    number = forms.IntegerField()
    paymode = forms.CharField(max_length=50)