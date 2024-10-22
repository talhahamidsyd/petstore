from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name="index"),
    path('savetocart/<int:id>/',views.savetocart,name="savetocart"),
    path('profile/',views.profile,name="profile"),
    path('search/',views.search,name="search"),
    path('cart/',views.cart,name="cart"),
    path('checkout/',views.checkout,name="checkout"),
    path('pay/',views.pay,name="pay"),
    path('orders/',views.orders,name="orders"),
    path('wishlist/',views.wishlist,name="wishlist"),
    path('product/',views.product,name="product"),    
    path('update_quantity/<int:id>/<str:action>/',views.update_quantity,name="update_quantity"),    
    path('buyapet/<int:id>/',views.buyapet,name="buyapet"),    
    path('buyallpets/',views.buyallpets,name="buyallpets"),    
    
    path('payment/<int:amount>/',views.payment,name="payment"),    
    path('success/<int:amount>/<int:id>/<str:payment_id>/<str:address>/',views.success,name="success"),
    

    # path('payment/<int:amount>/<str:name>/<str:quantity>/',views.pay,name="pay"),
    # path('success/<str:id>/<str:payment_id>/<str:order_id>/<str:signature>/<int:amount>/<int:bit_id>/',views.payment_success,name="payment_success"),

]
