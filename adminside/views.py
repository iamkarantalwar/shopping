from django.shortcuts import render,redirect
from django.http import HttpResponse
from.models import Register
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from.models import Category
from.models import Subcategory,Product,Order
import json
# Create your views here.

def dashboard(request):
    return render(request, "itcompany/dashboard.html")

def icons(request):
    return render(request, "itcompany/icons.html")

def map(request):
    return render(request, "itcompany/map.html")
@login_required(login_url='/itcompany/login/')

def shop1(request):
    return HttpResponse("hello world")


# @login_required(login_url='/itcompany/login/')

def form(request):
    if request.method == "POST":
        r = Register()
        r.email = request.POST['email']
        r.name = request.POST['name']
        r.password = request.POST['password']
        r.save()
        lis=[r.email,r.name,r.password]
        return HttpResponse("add successfully")
    else:

        return render(request,"itcompany/form1.html")

def loginpage(request):
    if request.method == "POST":
        result = authenticate(username=request.POST['user_name'],
                              password=request.POST['password1']
                              )
        if result is None:
            return HttpResponse("please check your details again")
        else:
            login(request,result)
            return HttpResponse("Accept")
    else:
        return render(request,"itcompany/login.html")

def logoutpage(request):
    logout(request)
    return HttpResponse("logged out")


def register (request):
    if request.method == "POST":
        User.objects.create_user(username=request.POST['username'],password=request.POST['password'])
        return HttpResponse("user created")
    else:
        return render(request,"itcompany/register.html")


def category(request):
    if request.method == "POST":
        
        c = Category()
        c.name = request.POST['category']
        c.image = request.FILES["image"]
        c.save()

        return HttpResponse("add successfully")
    else:

        return render(request,"itcompany/addcategory.html")

def subcategory(request):
    if request.method == "POST":
        c = Subcategory()
        c.category = Category.objects.get(id=request.POST['category'])
        c.name =request.POST['sub']
        c.save()
        
        return HttpResponse("add successfully")
    else:
        catgs =Category.objects.all()
        return render(request,"itcompany/subcategory.html",{'catgs':catgs})

def product(request):
    if request.method == "POST":
        c = Product()
        c.subcategory = Subcategory.objects.get(id=request.POST['subcategory'])
        c.name =request.POST['product']
        c.product_description =request.POST['product_description']
        c.original_price =request.POST['original_price']
        c.discount_price =request.POST['discount_price']
        c.image=request.FILES["file"]
        c.save()
        
        return HttpResponse("add successfully")
    else:
        subcatgs =Subcategory.objects.all()
        return render(request,"itcompany/product.html",{'subcatgs':subcatgs})
def order(request):
    if request.method == "POST":
        c = Order()
        c.userid = request.POST['userid']
        c.status =request.POST['status']
        c.final_amount =request.POST['final_amount']
        c.address =request.POST['address']
        c.products=request.POST['products']
        c.save()
        
        return HttpResponse("add successfully")
    else:
        orders = Order.objects.all()

        return render(request,"itcompany/order.html",{"orders":orders})

def viewcategory(request):
    categories = Category.objects.all()
    return render(request,"itcompany/viewcategory.html",{"categories":categories})


def vieworder(request,pk):
    if request.method=="POST":
        orde = Order.objects.get(id=pk)
        orde.status = request.POST["status"]
        orde.save()
        return redirect(order)

    else:
        orde = Order.objects.get(id=pk)
        order_details = {}
        total =0 
        for i,j in (json.loads(orde.products)).items():
            
            order_details.update(
                {
                Product.objects.get(id=i): {j:
                                    {"total":int(j)*int(Product.objects.get(id=i).discount_price)}}
                }
                )
            total += int(j)*int(Product.objects.get(id=i).discount_price)
        print(total)
        print(order_details)
        
        return render(request,"itcompany/vieworder.html",{"order":orde,"order_details":order_details,"total":total})


def editcategory(request,pk):
    if request.method=="POST":
        c = Category.objects.get(id=pk)
        c.name = request.POST['cat']
        c.save()
        return HttpResponse("Data Saved")
    else:
        cat=Category.objects.get(id=pk)
        return render(request,"itcompany/editcategory.html",{"cat":cat})

def delcategory(request,pk):
        d = Category.objects.get(id=pk)
        d.delete()
        return redirect(viewcategory)    