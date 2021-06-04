from django.contrib import admin
from .models import Order, Customer, Food, User
# Register your models here.

admin.site.register(Order)
admin.site.register(Customer)
admin.site.register(Food)
admin.site.register(User)