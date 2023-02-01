from django.urls import path
from .views import *

urlpatterns = [
    path('index/', index),
    path('userprofile/', newproductsdisplay),
    path('userreg/', userregistration),
    path('userlogin/', userlogin),
    path('sellerreg/', sellerregistration),
    path('sellerlogin/', sellerlogin),
    path('sellerprofile/', sellerprofile),
    path('addproducts/', addproducts),
    path('newproducts/', newproductsdisplay),
    path('addtowishlist/<int:id>', addtowishlistt),
    path('wishlistdisplay/', wishlistdisplay),
    path('wishlisttocart/<int:id>', wishlisttocart),
    path('removewishlist/<int:id>', wishlistdelete),
    path('addtocart/<int:id>', addtocart),
    path('cartdisplay/', cartdisplay),
    path('cartpayment/<int:id>', cartpayment),
    path('removecart/<int:id>', cartdelete),
    path('edituser/<int:id>', useredit),
    path('deleteuser/<int:id>', userdelete),
    path('editseller/<int:id>', selleredit),
    path('deleteseller/<int:id>', sellerdelete),
    path('payment/<int:id>', payment),
    path('soldproducts/<int:id>', soldproducts),
    path('search/', searchresult),

]