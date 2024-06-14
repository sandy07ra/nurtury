from django.shortcuts import render,redirect
from django.views.generic import View,ListView,CreateView
from Nurture.models import Category,Subcategory,Product,Cart,Order
from django.contrib.auth.models import User
from Nurture.forms import registration_form,login_form,order_form
from django.urls import reverse_lazy
from django.contrib.auth import authenticate,login,logout
from django.utils.decorators import method_decorator

# Create your views here.

# decorators
def signin_required(fn):
    def wrapper(self,request,*args,**kwargs):
        if not request.user.is_authenticated:
            return redirect("login")
        else:
            return fn(self,request,*args,**kwargs)
    return wrapper

# --Registration--
class Registration_view(CreateView):
    template_name="Nurture/registration.html"
    form_class=registration_form
    model=User
    success_url=reverse_lazy("login")

# --Authentication--    
class Login_view(View):
    def get(self,request,*args,**kwargs):
        form=login_form()
        return render(request,"Nurture/login.html",{"form":form})
    
    def post(self,request,*args,**kwargs):
        form=login_form(request.POST)
        if form.is_valid():
            u_name=form.cleaned_data.get("username")
            pwd=form.cleaned_data.get("password")
            user_obj=authenticate(request,username=u_name,password=pwd)
            if user_obj:
                login(request,user_obj)
                print("success")
                return redirect("home")
            else:
                print("error")
                return redirect("login")

class Logout(View):
    def get(self,request,*args,**kwargs):
        logout(request)
        return redirect("home")

# --Category--
class Home(ListView):
    template_name="Nurture/index.html"
    model=Category
    context_object_name="categories"

# --Subcategory--
class Subcategory_view(View):
    def get(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        data=Subcategory.objects.filter(category_id=id)
        name=Category.objects.get(id=id)
        return render(request,"Nurture/subcategory.html",{"data":data,"name":name})
    
# --Product--    
class Products(View):
    def get(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        data=Product.objects.filter(subcategory_id=id)
        name=Subcategory.objects.get(id=id)
        return render(request,"Nurture/product.html",{"data":data,"name":name})
    
class Product_detail(View):
    def get(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        data=Product.objects.get(id=id)
        return render(request,"Nurture/product_detail.html",{"data":data})
    
# --Cart--    
class AddToCart(View):
    def get(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        data=Product.objects.get(id=id)
        Cart.objects.create(item=data,user=request.user)
        print("successful")
        return redirect("product_detail",pk=id)


class cart(View):
    def get(self,request,*args,**kwargs):
        data=Cart.objects.filter(user=request.user)
        return render(request,"Nurture/cart.html",{"data":data})
    
# class cart_detail(View):
#     def get(self,request,*args,**kwargs):
#         id=kwargs.get("pk")
#         data=Cart.objects.get(id=id)
#         return render(request,"Nurture/cart_detail.html",{"data":data})

class cart_delete(View):
    def get(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        Cart.objects.get(id=id).delete()
        return redirect("cart")

# --Order--    
class order(View):
    def get(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        data=Product.objects.get(id=id)
        form=order_form()
        return render(request,"Nurture/order.html",{"form":form,"data":data})
    
    def post(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        data=Product.objects.get(id=id)
        form=order_form(request.POST)
        if form.is_valid():
            qs=form.cleaned_data.get("address")
            Order.objects.create(address=qs,order_item=data,customer=request.user)
            return redirect("cart",pk=id)
        else:
            print("error")
        return redirect("cart")


class view_order(View):
    def get(self,request,*args,**kwargs):
        data=Order.objects.filter(customer=request.user)
        return redirect("Nurture/order_view.html",{"data":data})
    
class order_delete(View):
    def get(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        Order.objects.get(id=id).delete()
        return redirect("view_order")
        
        



