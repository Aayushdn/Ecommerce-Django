from django.urls import path
from . import views



urlpatterns = [
    path('', views.index , name="ShopHome"),
    path('about/', views.about , name="AboutUs"),
    path('contact/', views.contact , name="ContactUs"),
    path('Products/<int:myid>', views.ProductView , name="ProductView"),
    path('search/', views.search , name="Search"),
    path('tracker/',views.tracker,name="tracker"),
    path('checkout/',views.checkout , name="checkout"),
    path('verifyPayment/' , views.verifyPayment, name = "verifyPayment")
]
