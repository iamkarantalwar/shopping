from django.shortcuts import render,redirect
from django.http import HttpResponse
from adminside.models import *
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login,authenticate,logout
import json
from django.db.models import Q
# Create your views here.
cats = Category.objects.all()
def base(request):
    subact = Subcategory.objects.all()[0:4]
    return render(request,"userside/home.html",{'cats':cats,'subcats':subact})

def products(request,pk):

    sub = Subcategory.objects.get(id=pk)
    pro = Product.objects.filter(subcategory_id=pk)
    return render(request,"userside/womens.html",{'products':pro,'cats':cats,"sub":sub})

def womenproduct(request,wp):
    if request.method == "POST":
        if request.session.get("cart") is None:
            request.session["cart"] = {request.POST['id']:request.POST['quantity']}
            print(request.session.get("cart"))
        else:
            d = {request.POST['id']:request.POST['quantity']}
            request.session.modified = True
            request.session["cart"].update(d)
            print(request.session.get("cart"))
        return redirect(showcart)

    else:    
        pro = Product.objects.get(id=wp)
        return render(request,"userside/single.html",{'product':pro,'wp':wp,'cats':cats})

#def single(request,pk):
     #return render(request,"userside/single.html")

# def mens(request):
#      return render(request,"userside/mens.html")

def product(request):
    if request.method == "POST":
        c = Product()
        c.subcategory = Subcategory.objects.get(id=request.POST['subcategory'])
        c.name =request.POST['product']
        c.product_description =request.POST['product_description']
        c.original_price =request.POST['original_price']
        c.discount_price =request.POST['discount_price']
        c.save()
        
        return HttpResponse("add successfully")
    else:
        subcatgs =Subcategory.objects.all()
        return render(request,"itcompany/product.html",{'subcatgs':subcatgs,'cats':cats})

def add_to_cart(request,mk):
    pro = Product.objects.filter(subcategory_id=mk)
    return render(request,"userside/single.html",{'products':pro,'mk':cats,'cats':cats,})

def showcart(request):
    try:
        cart = request.session.get("cart")
        newcart = {}
        for i,j in cart.items():
            #print(i)
            newcart.update({Product.objects.get(id=i):j})
        print(newcart)
        return render(request,"userside/showcart.html",{"cart":newcart,'cats':cats,})
    except:
        return render(request,"userside/showcart.html")

def signup(request):
    User.objects.create_user(
            username=request.POST['email'],
            password=request.POST['password'],
            email=request.POST['email'],
            first_name=request.POST['name']
    )
    return HttpResponse("User Created")

def signin(request):
    user = authenticate(username=request.POST["email"],
                        password=request.POST['password'])
    if user is None:
        return HttpResponse("Enter correct Credentials")
    else:
        login(request,user)
        return HttpResponse("User is now Sign In")


def signout(request):
    logout(request)
    return HttpResponse("User Logged Out")

def delfromcart(request,pk):
    request.session.modified = True
    a = request.session.get("cart")
   
    request.session["cart"].pop(pk)
    return redirect(showcart)


@login_required(login_url="/")
def checkout(request):
    if request.method=="POST":
        o = Order()
        o.userid = User.objects.get(id=request.user.id)
        o.phno = request.POST["telephone"]
        o.address = request.POST["address"]
        o.city = request.POST["city"]
        o.pincode = request.POST['pincode']
        o.state = request.POST["state"]
        o.status="PENDING"
        o.final_amount="FINAL AMOUNT"
        o.products = json.dumps(request.session["cart"])
        o.save()
        request.session.modified = True
        del request.session["cart"]
        return HttpResponse("Product is on Deleviry")
    else:
        user = User.objects.get(id=request.user.id)
        return render(request,"userside/checkout.html",{"user":user,'cats':cats})

@login_required(login_url="/")
def history(request):
    orders = Order.objects.filter(userid=request.user)
    return render(request,"userside/history.html",{"orders":orders,'cats':cats,})

def viewdetails(request,id):
    order = Order.objects.get(id=id)
    order_details = {}
    total =0 
    for i,j in (json.loads(order.products)).items():
        order_details.update(
            {
            Product.objects.get(id=i): {j:
                                {"total":int(j)*int(Product.objects.get(id=i).original_price)}}
            }
            )
        total += int(j)*int(Product.objects.get(id=i).original_price)
    print(order_details)
    return render(request,"userside/vieworder.html",{"order":order,"order_details":order_details,"total":total,'cats':cats,})

def search(request):
    q = request.GET["q"]
    pro = Product.objects.filter(
        Q(name__icontains=q)|
        Q(subcategory__name__icontains=q)
    )
    return render(request,"userside/womens.html",{'products':pro,'cats':cats,})