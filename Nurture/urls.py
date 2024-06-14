from django.urls import path
from Nurture import views

urlpatterns=[
    path("registration/",views.Registration_view.as_view(),name="registration"),
    path("login/",views.Login_view.as_view(),name="login"),
    path("logout/",views.Logout.as_view(),name="logout"),
    path("home/",views.Home.as_view(),name="home"),
    path("category_detail/<int:pk>",views.Subcategory_view.as_view(),name="category_detail"),
    path("subcategory_detail/<int:pk>",views.Products.as_view(),name="subcategory_detail"),
    path("product_detail/<int:pk>",views.Product_detail.as_view(),name="product_detail"),
    path("addtocart/<int:pk>",views.AddToCart.as_view(),name="addtocart"),
    path("cart",views.cart.as_view(),name="cart"),
    path("cart_delete/<int:pk>",views.cart_delete.as_view(),name="cart_delete"),
    # path("cart_detail/<int:pk>",views.cart_detail.as_view(),name="cart_detail"),
    path("order/<int:pk>",views.order.as_view(),name="order"),
    path("view_order/",views.view_order.as_view(),name="view_order"),
    path("order_delete/<int:pk>",views.order_delete.as_view(),name="order_delete"),
    
    
]