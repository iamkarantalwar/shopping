from django.db import models

# Create your models here.
class Register(models.Model):
    email = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    password = models.CharField(max_length=200)

class Category(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to="products/")

    def __str__(self):
        return self.name

class Subcategory(models.Model):
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    name=models.CharField(max_length=200)

class Product(models.Model):
    subcategory=models.ForeignKey(Subcategory,on_delete=models.CASCADE)
    name=models.CharField(max_length=200)
    product_description=models.CharField(max_length=200)
    original_price=models.CharField(max_length=200)
    discount_price=models.CharField(max_length=200)
    image = models.ImageField(upload_to="products/")

class Order(models.Model):
    userid=models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    state = models.CharField(max_length=200)
    phno = models.CharField(max_length=200)
    pincode = models.CharField(max_length=200)
    status=models.CharField(max_length=200)
    final_amount=models.CharField(max_length=200)
    address=models.CharField(max_length=200)
    products=models.CharField(max_length=200)

class Payment_detail(models.Model):
    order_id=models.CharField(max_length=200)
    payment_type=models.CharField(max_length=200)
    card_no=models.CharField(max_length=200)
    cvv=models.CharField(max_length=200)
    expiry_date = models.CharField(max_length=200)
    card_holder = models.CharField(max_length=200)

class Register_again(models.Model):
    username=models.CharField(max_length=200)
    password=models.CharField(max_length=200)



