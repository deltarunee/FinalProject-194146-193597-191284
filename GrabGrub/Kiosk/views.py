from django.shortcuts import render, redirect, get_object_or_404
from .models import User, Customer, Food, Order
from django.contrib import messages
# Create your views here.

useraccount = User.objects.get(pk=1)

def login(request):
    if(request.method == "POST"):
        user = request.POST.get('username')
        passw = request.POST.get('password')

        
        userlist = User.objects.filter(username = user)

        if(len(userlist) > 0):
           
            authorize = User.objects.get(username = user)

            if(authorize.getPassword() == passw):
                global useraccount
                useraccount = authorize
                messages.success(request, 'Log in Successful!')
                return redirect('order')

            else:
                messages.info(request, 'Invalid Login')
                return render(request, 'Kiosk/login.html')

        else:
            messages.info(request, 'Invalid Login')
            return render(request, 'Kiosk/login.html')

    else: 
        return render(request,'Kiosk/login.html')

def base(request):
    return render(request,'Kiosk/base.html')

def order(request):
    order_object = Order.objects.all()
    return render(request, 'Kiosk/order.html', {'Orders':order_object})
    
def accountcreation(request):
    if(request.method == "POST"):
        user = request.POST.get('username')
        passw = request.POST.get('password')
        userlist = User.objects.filter(username = user)

        if(len(userlist) > 0):
            messages.info(request, 'User already exists')
            return render(request, 'Kiosk/accountcreation.html')
        else:
            User.objects.create(username = user, password = passw)
            messages.info(request, 'Account Created')
            return redirect('login')
    else:
        return render(request, 'Kiosk/accountcreation.html')
    
def fooditems(request):
    return render(request, 'Kiosk/fooditems.html')

def add_order(request):
    if(request.method == "POST"):
        customername = get_object_or_404(Customer, pk=request.POST.get('cname'))
        numberfood = request.POST.get('nfood')
        foodname = get_object_or_404(Food, pk=request.POST.get('fname'))
        paymentMode = request.POST.get('pMode')

        Order.objects.create(cust_order = customername, food = foodname, qty = numberfood, payment_mode = paymentMode)
        messages.success(request, 'Order Created')
        return redirect('order')
    else:
        food = Food.objects.all()
        customer = Customer.objects.all()

        return render(request, 'Kiosk/add_order.html', {'food':food , 'customer':customer})

def order_detail(request, pk):
    B = get_object_or_404(Order, pk=pk)
    return render(request, 'Kiosk/order_detail.html', {'d': B})

def order_update(request, pk):
    if(request.method == "POST"):
        qty = request.POST.get('qty')
        payment = request.POST.get('payment_update')
        
        Order.objects.filter(pk=pk).update(qty = qty, payment_mode = payment)

        return redirect('order_detail', pk=pk)
    else:
	    d = get_object_or_404(Order, pk=pk)
	    return render(request, 'Kiosk/order_update.html', {'d':d})
            

def order_delete(request, pk):
        Order.objects.filter(pk=pk).delete()
        return redirect('order')

def food(request):
    food_object = Food.objects.all()
    return render(request, 'Kiosk/food.html', {'Food':food_object})

def customer(request):
    customer_object = Customer.objects.all()
    return render(request, 'Kiosk/customer.html', {'Customer':customer_object})

def customer_detail(request, pk):
    d = get_object_or_404(Customer, pk=pk)
    return render(request, 'Kiosk/customer_detail.html', {'d':d})

def food_detail(request, pk):
    d = get_object_or_404(Food, pk=pk)
    return render(request, 'Kiosk/food_detail.html', {'d':d})

def add_food(request):
    if(request.method == "POST"):
        name = request.POST.get('name')
        namecomparison = name.upper()
        description = request.POST.get('desc')
        price = request.POST.get('price')
        
        foodlist = Food.objects.filter(name__iexact = name)
        if len(foodlist) > 0:
            messages.info(request, 'Food already exists')
            return redirect('add_food')
            
        # if(len(foodlist) > 0):
        #     messages.info(request, 'Food already Exists')
        #     return redirect('add_food')
        else:
            messages.success(request, 'Added Food')
            Food.objects.create(name = name, description = description, price = price)

            return redirect('food')
    else:
        return render(request, 'Kiosk/add_food.html')

def food_delete(request, pk):
    Food.objects.filter(pk=pk).delete()
    return redirect('food')


def food_update(request, pk):
    if(request.method == "POST"):
        name = request.POST.get('name')
        namecomparison = name.upper()
        description = request.POST.get('desc')
        price = request.POST.get('price')

        foodlist = Food.objects.filter(name__iexact = name) 
        if len(foodlist) > 0:
            if name == foodlist[0].getName(): 
                Food.objects.filter(pk=pk).update(description = description, price = price)
                return redirect('food_detail', pk=pk)
            elif foodlist[0].getName().upper() == namecomparison:
                messages.info(request, 'Inputted the same food')
                return redirect('food_update', pk=pk)
        else:
            Food.objects.filter(pk=pk).update(name = name, description = description, price = price)
            return redirect('food_detail', pk=pk)
        
    else:
	    d = get_object_or_404(Food, pk=pk)
	    return render(request, 'Kiosk/food_update.html', {'d':d})

def customer_delete(request, pk):
    Customer.objects.filter(pk=pk).delete()
    return redirect('customer')

def customer_update(request, pk):
    if(request.method == "POST"):
        name = request.POST.get('name')
        namecomparison = name.upper()
        address = request.POST.get('address')
        city = request.POST.get('city')

        customerlist = Customer.objects.filter(name__iexact = name) 
        if len(customerlist) > 0:
            if name == customerlist[0].getName(): 
                Customer.objects.filter(pk=pk).update(address = address, city = city)
                return redirect('customer_detail', pk=pk)
            elif customerlist[0].getName().upper() == namecomparison:
                messages.info(request, 'Inputted the same customer')
                return redirect('customer_update', pk=pk)
        else:
            Customer.objects.filter(pk=pk).update(name = name, address = address, city = city)
            return redirect('customer_detail', pk=pk)
    else:
	    d = get_object_or_404(Customer, pk=pk)
	    return render(request, 'Kiosk/customer_update.html', {'d':d})

        
def add_customer(request):
    if(request.method == "POST"):
        name = request.POST.get('name')
        address = request.POST.get('address')
        city = request.POST.get('city')
        
        customerlist = Customer.objects.filter(name__iexact = name)

        if(len(customerlist) > 0):
            messages.info(request, 'Customer already Exists')
            return redirect('add_customer')
        else:
            messages.success(request, 'Added Customer')
            Customer.objects.create(name = name, address = address, city = city)

        return redirect('customer')
    else:
        return render(request, 'Kiosk/add_customer.html')
