from django.urls import path
from . import views
urlpatterns= [
path('',views.home,name='home'),
path('userpage/',views.userPage,name='userpage'),
path('register/',views.registerPage,name='register'),
path('logout/',views.logoutUser,name='logout'),
path('login/',views.loginPage,name='login'),
path('customers/<str:cust_id>',views.customers,name='customer'),
path('products/',views.products,name='products'),
path('create_order/<str:pk>',views.createOrder,name='create_order'),
path('update_order/<str:pk>', views.updateOrder, name='update_order'),
path('delete_order/<str:pk>',views.deleteOrder, name='delete_order'),
]