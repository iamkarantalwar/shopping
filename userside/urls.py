from django.contrib import admin
from django.urls import path,include
from.import views

urlpatterns = [
    path('', views.base,name="home"),
    path('products/<int:pk>',views.products,name="products"),
    path('womenproduct/<int:wp>',views.womenproduct,name="womenproduct"),
    path("add_to_cart/<int:pk>",views.add_to_cart,name="add_to_cart"),
    path("showcart/",views.showcart,name="showcart"),
    path("signup/",views.signup,name="signup"),
    path("signin/",views.signin,name="signin"),
    path("signout/",views.signout,name="signout"),
    path("delfromcart/<str:pk>",views.delfromcart,name="delfromcart"),
    path("checkout/",views.checkout,name="checkout"),
    path("history/",views.history,name="history"),
    path("viewdetails/<int:id>",views.viewdetails,name="viewdetails"),
    path("search/",views.search,name="search")
    
]
