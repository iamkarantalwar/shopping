from django.contrib import admin
from django.urls import path,include
from.import views

urlpatterns = [
    path('', views.dashboard),
    path('icons/', views.icons),
    path('map/', views.map),
    path("form/",views.form),
    path("login/", views.loginpage,name="loginpage"),
    path("logout/", views.logoutpage,name="logoutpage"),
    path("register/",views.register,name="register"),
    path("category/",views.category,name="addcategory"),
    path("subcategory/",views.subcategory,name="subcategory"),
    path("product/",views.product,name="product"),
    path("order/",views.order,name="order"),
    path("viewcategory/",views.viewcategory,name="viewcategory"),
    path("order/<int:pk>",views.vieworder,name="vieworder"),
    path("editcategory/<int:pk>",views.editcategory,name="editcategory"),
    path("delcategory/<int:pk>",views.delcategory,name="delcategory")
  
    
    
]
