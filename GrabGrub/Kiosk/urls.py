"""GrabGrub URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.login, name='login'),
    path('base', views.base, name='base'),
    path('accountcreation', views.accountcreation, name='accountcreation'),
    path('order', views.order, name='order'),
    path('order_detail/<int:pk>/', views.order_detail, name='order_detail'),
    path('order_update/<int:pk>/', views.order_update, name='order_update'),
    path('order_delete/<int:pk>/', views.order_delete, name='order_delete'),
    path('add_order', views.add_order, name='add_order'),
    path('customer', views.customer, name='customer'),
    path('food', views.food, name='food'),
    path('food_detail/<int:pk>/', views.food_detail, name='food_detail'),
    path('food_delete/<int:pk>/', views.food_delete, name='food_delete'),
    path('add_food', views.add_food, name='add_food'),
    path('customer_detail/<int:pk>/', views.customer_detail, name='customer_detail'),
    path('food_update/<int:pk>/', views.food_update, name='food_update'),
    path('customer_update/<int:pk>/', views.customer_update, name='customer_update'),
    path('customer_delete/<int:pk>/', views.customer_delete, name='customer_delete'),
    path('add_customer', views.add_customer, name='add_customer'),

]
