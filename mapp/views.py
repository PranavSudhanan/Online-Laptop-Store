from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import ListView

from .models import *
from .forms import *
from mproject.settings import EMAIL_HOST_USER


# Create your views here.

def index(request):
    a = addproductmodel.objects.all()
    im = []
    pname = []
    price = []
    for i in a:
        img = i.image
        im.append(str(img).split('/')[-1])
        nm = i.pname
        pr = i.price
        pname.append(nm)
        price.append(pr)
    mylist = zip(im, pname, price)
    return render(request,'index.html', {'list': mylist})


def userregistration(request):
    if request.method=='POST':
           un=request.POST.get("username")
           em=request.POST.get("email")
           ps=request.POST.get("password")
           cps=request.POST.get("cpassword")
           if ps==cps:
                b = User(username=un, email=em, password=ps)
                b.save()
                return redirect(userlogin)
           else:
               return HttpResponse("Registration Failed!")
    else:
        return render(request,'userregistration.html')


def userlogin(request):
    if request.method == 'POST':
        a = userlogform(request.POST)
        if a.is_valid():
            em = a.cleaned_data['email']
            ps = a.cleaned_data['password']
            b = User.objects.all()
            for i in b:
                usr = i.username
                if i.email == em and i.password == ps:
                    # return HttpResponse("Login Success")
                    a = addproductmodel.objects.all()
                    im = []
                    pname = []
                    price = []
                    id = []
                    for i in a:
                        id1 = i.id
                        id.append(id1)
                        img = i.image
                        im.append(str(img).split('/')[-1])
                        nm = i.pname
                        pr = i.price
                        pname.append(nm)
                        price.append(pr)
                    mylist = zip(im, pname, price, id)
                    return render(request, "userprofile.html", {'usr':usr, 'list':mylist})
            else:
                return HttpResponse("Login failed")
    else:
        return render(request, 'userlogin.html')


# def userprofile(request):
#     return render(request, 'userprofile.html')

def useredit(request, id):
    a = User.objects.get(id=id)
    if request.method == 'POST':
        a.username = request.POST.get("username")
        a.email = request.POST.get("email")
        a.password = request.POST.get("password")
        a.save()
        return redirect(userlogin)
    return render(request, 'edituser.html', {'a': a})


def userdelete(request, id):
    a = User.objects.get(id=id)
    a.delete()
    return HttpResponse("Account Deleted Successfully")


def sellerregistration(request):
    if request.method=='POST':
        a = sellerregform(request.POST)
        if a.is_valid():
            nm = a.cleaned_data['companyname']
            em = a.cleaned_data['email']
            ph = a.cleaned_data['number']
            ps = a.cleaned_data['password']
            cp = a.cleaned_data['cpassword']
            ad = a.cleaned_data['address']
            if ps==cp:
                b = sellerregmodel(companyname=nm, email=em, number=ph, password=ps, address=ad)
                b.save()
                # return HttpResponse("Registration Success....")
                return redirect(sellerlogin)
            else:
                return HttpResponse("Incorrect Password!")
        else:
            return HttpResponse("Registration Failed!")
    else:
        return render(request,'sellerregistration.html')


def sellerlogin(request):
    if request.method == 'POST':
        a = sellerlogform(request.POST)
        if a.is_valid():
            em = a.cleaned_data['email']
            ps = a.cleaned_data['password']
            b = sellerregmodel.objects.all()
            for i in b:
                cmp = i.companyname
                request.session['companyname'] = cmp
                id = i.id
                if i.email == em and i.password == ps:
                    # return HttpResponse("Login Success")
                    return render(request, 'sellerprofile.html',{'cmp':cmp, 'id':id})
            else:
                return HttpResponse("Login failed")
    else:
        return render(request, 'sellerlogin.html')

def selleredit(request, id):
    a = sellerregmodel.objects.get(id=id)
    if request.method == 'POST':
        a.companyname = request.POST.get("companyname")
        a.email = request.POST.get("email")
        a.number = request.POST.get("number")
        a.password = request.POST.get("password")
        a.address = request.POST.get("address")
        a.save()
        return redirect(sellerlogin)
    return render(request, 'editseller.html', {'a': a})

def sellerdelete(request, id):
    a = sellerregmodel.objects.get(id=id)
    a.delete()
    return HttpResponse("Account Deleted Successfully")


def sellerprofile(request):
    return render(request, 'sellerprofile.html')


def addproducts(request):
    if request.method == 'POST':
        a = addproductform(request.POST, request.FILES)
        if a.is_valid():
            ig = a.cleaned_data['image']
            nm = a.cleaned_data['pname']
            pr = a.cleaned_data['price']
            b = addproductmodel(image=ig, pname=nm, price=pr)
            b.save()
            # return HttpResponse("Product Uploaded Successfully...")
            return redirect(newproductsdisplay)
        else:
            return HttpResponse("Product Upload failed!")
    return render(request, 'addproducts.html')


def newproductsdisplay(request):
    a = addproductmodel.objects.all()
    im = []
    pname = []
    price = []
    id = []
    for i in a:
        id1 = i.id
        id.append(id1)
        img = i.image
        im.append(str(img).split('/')[-1])
        nm = i.pname
        pr = i.price
        pname.append(nm)
        price.append(pr)
    mylist = zip(im, pname, price, id)
    return render(request, 'userprofile.html', {'list': mylist})



def addtowishlistt(request, id):
    a = addproductmodel.objects.get(id=id)
    b = wishlistmodel(image=a.image, pname=a.pname, price=a.price)
    b.save()
    # return HttpResponse("Product added to Cart")
    return redirect(wishlistdisplay)


def wishlistdisplay(request):
    a = wishlistmodel.objects.all()
    im = []
    pname = []
    price = []
    id = []
    for i in a:
        id1 = i.id
        id.append(id1)
        img = i.image
        im.append(str(img).split('/')[-1])
        nm = i.pname
        pr = i.price
        pname.append(nm)
        price.append(pr)
    mylist = zip(im, pname, price, id)
    return render(request, 'wishlistdisplay.html', {'a':a, 'list':mylist})


def wishlisttocart(request, id):
    a = wishlistmodel.objects.get(id=id)
    b = cartmodel(image=a.image, pname=a.pname, price=a.price)
    b.save()
    # return HttpResponse("Product added to Cart")
    return redirect(cartdisplay)


def wishlistdelete(request,id):
    a = wishlistmodel.objects.get(id=id)
    a.delete()
    return redirect(wishlistdisplay)




def addtocart(request, id):
    a = addproductmodel.objects.get(id=id)
    b = cartmodel(image=a.image, pname=a.pname, price=a.price)
    b.save()
    # return HttpResponse("Product added to Cart")
    return redirect(cartdisplay)


def cartdisplay(request):
    a = cartmodel.objects.all()
    im = []
    pname = []
    price = []
    id = []
    for i in a:
        id1 = i.id
        id.append(id1)
        img = i.image
        im.append(str(img).split('/')[-1])
        nm = i.pname
        pr = i.price
        pname.append(nm)
        price.append(pr)
    mylist = zip(im, pname, price, id)
    return render(request, 'cartdisplay.html', {'a':a, 'list':mylist})


def cartpayment(request, id):
    b = cartmodel.objects.get(id=id)
    pnm = b.pname
    prc = b.price
    if request.method == 'POST':
        a = paymentform(request.POST)
        if a.is_valid():
            pn = a.cleaned_data['pname']
            pr = a.cleaned_data['price']
            fn = a.cleaned_data['fname']
            ad = a.cleaned_data['address']
            em = a.cleaned_data['email']
            nm = a.cleaned_data['number']
            pm = a.cleaned_data['paymode']
            b = paymentmodel(pname=pn, price=pr, fname=fn, address=ad, email=em, number=nm, paymode=pm)
            b.save()
            subject = f"Order Placed for {pn}"
            message = f"hello {fn}\n your order for {pn} is placed successfully. Expect delivery within next week\n\n Order Details:\n Product Name: {pn}\n MRP: {pr} INR\n Customer Details:\n Name: {fn}\n Address: {ad}\n Number: {nm}\n Payment Mode: {pm}"
            email_from = EMAIL_HOST_USER
            send_mail(subject, message, email_from, [em])
            return render(request, 'ordersuccess.html')
            # return HttpResponse("Order Placed....")
        else:
            return HttpResponse("Order Failed!")
    else:
        return render(request, 'buyproduct.html', {'pnm':pnm, 'prc':prc})


def cartdelete(request,id):
    a = cartmodel.objects.get(id=id)
    a.delete()
    return redirect(cartdisplay)


def payment(request, id):
    b = addproductmodel.objects.get(id=id)
    pnm = b.pname
    prc = b.price
    if request.method == 'POST':
        a = paymentform(request.POST)
        if a.is_valid():
            pn = a.cleaned_data['pname']
            pr = a.cleaned_data['price']
            fn = a.cleaned_data['fname']
            ad = a.cleaned_data['address']
            em = a.cleaned_data['email']
            nm = a.cleaned_data['number']
            pm = a.cleaned_data['paymode']
            b = paymentmodel(pname=pn, price=pr, fname=fn, address=ad, email=em, number=nm, paymode=pm)
            b.save()
            subject = f"Order Placed for {pn}"
            message = f"hello {fn}\n your order for {pn} is placed successfully. Expect delivery within next week\n\n Order Details:\n Product Name: {pn}\n MRP: {pr} INR\n Customer Details:\n Name: {fn}\n Address: {ad}\n Number: {nm}\n Payment Mode: {pm}"
            email_from = EMAIL_HOST_USER
            send_mail(subject, message, email_from, [em])
            return render(request, 'ordersuccess.html')
            # return HttpResponse("Order Placed....")
        else:
            return HttpResponse("Order Failed!")
    else:
        return render(request, 'buyproduct.html', {'pnm':pnm, 'prc':prc})


def soldproducts(request, id):
    a = paymentmodel.objects.all()
    pname = []
    price = []
    fname = []
    address = []
    email = []
    number = []
    paymode = []
    id = []
    for i in a:
        id1 = i.id
        id.append(id1)
        nm = i.pname
        pr = i.price
        fn = i.fname
        ad = i.address
        em = i.email
        nr = i.number
        pm = i.paymode
        pname.append(nm)
        price.append(pr)
        fname.append(fn)
        address.append(ad)
        email.append(em)
        number.append(nr)
        paymode.append(pm)
    mylist = zip(pname, price, fname, address, email, number, paymode, id)
    return render(request, 'soldproducts.html', {'a':a, 'list':mylist})



def searchresult(request):

    query = request.GET.get("query", "")
    a = addproductmodel.objects.filter(pname__icontains=query)
    return render(request, 'searchresults.html', {'a': a})

