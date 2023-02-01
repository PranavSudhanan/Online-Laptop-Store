from django.db import models

# Create your models here.

class sellerregmodel(models.Model):
    companyname = models.CharField(max_length=25)
    email = models.EmailField()
    password = models.CharField(max_length=20)
    number = models.IntegerField()
    address = models.CharField(max_length=100)


class addproductmodel(models.Model):
    image = models.ImageField(upload_to='mapp/static')
    pname = models.CharField(max_length=25)
    price = models.IntegerField()


class wishlistmodel(models.Model):
    image = models.ImageField(upload_to='mapp/static')
    pname = models.CharField(max_length=25)
    price = models.IntegerField()


class cartmodel(models.Model):
    image = models.ImageField(upload_to='mapp/static')
    pname = models.CharField(max_length=25)
    price = models.IntegerField()


class paymentmodel(models.Model):
    choice = [
        ('Debit/Credit Card','Debit/Credit Card'),
        ('Upi','Upi'),
        ('Cash on delivery','Cash on delivery'),
    ]

    pname = models.CharField(max_length=50)
    price = models.CharField(max_length=20)
    fname = models.CharField(max_length=20)
    address = models.CharField(max_length=50)
    email = models.EmailField()
    number = models.IntegerField()
    paymode = models.CharField(max_length=50, choices=choice)