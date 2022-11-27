from django.shortcuts import render,redirect
from django.forms import inlineformset_factory 
from django.http import HttpResponse
from .orderForm import OrderForm, CreateUser
from .models import Customer,Product,Order
from .filters import OrderFilter
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .decorators import authenticated_user,allowed_user,admin_only
from django.contrib.auth.models import Group

# Create your views here.


@login_required(login_url='login')
@admin_only

def home(request):
	Pending= Order.objects.filter(status='Pending').count()

	Total_order=Order.objects.all()

	Delivered= Order.objects.filter(status='Delivered').count()

	Out_for_delivery=Order.objects.filter(status='Out For Delivery').count()

	Customers=Customer.objects.all()

	contents={'Pending':Pending,'Out_for_delivery':Out_for_delivery,
	'Delivered':Delivered,'Customers':Customers,'Total_order':Total_order}

	return render(request,'accounts/dashboard.html',contents)

@login_required(login_url='login')
@allowed_user(allowed_role=['admin'])
def customers(request,cust_id):

	customer=Customer.objects.get(id=cust_id)

	orderedby_customer=customer.order_set.all()
	orderfilter=OrderFilter(request.GET,queryset=orderedby_customer)
	orderedby_customer=orderfilter.qs
	order_count=orderedby_customer.count()

	context={'customer':customer,'order_count':order_count,'orderfilter':orderfilter,
	'orders':orderedby_customer}

	return render(request, 'accounts/customers.html',context)

@login_required(login_url='login')
@allowed_user(allowed_role=['admin'])
def products(request):

	Products=Product.objects.all()

	return render(request,'accounts/products.html',{'Products':Products})
@login_required(login_url='login')
@allowed_user(allowed_role=['admin'])
def createOrder(request,pk):

	customer=Customer.objects.get(id=pk)

	Orderformset=inlineformset_factory(Customer,Order,fields=('product','status',),extra=10)

	formset=Orderformset(queryset=Order.objects.none(),instance=customer)

	#form=OrderForm(initial={'customer':customer})
	if request.method=='POST':
		formset=Orderformset(request.POST,instance=customer)
		if formset.is_valid():
			formset.save()
			return redirect('/')
	return render(request,'accounts/create_order.html',{'formset':formset})

@login_required(login_url='login')
@allowed_user(allowed_role=['admin'])
def updateOrder(request,pk):
	order=Order.objects.get(id=pk)

	form=OrderForm(instance=order)

	if request.method=='POST':
		form=OrderForm(request.POST, instance=order)
		if form.is_valid():
			form.save()
			return redirect('/')
	context={'form':form}
	return render(request,'accounts/create_order.html',context)

@login_required(login_url='login')
@allowed_user(allowed_role=['admin'])
def deleteOrder(request,pk):
	order=Order.objects.get(id=pk)
	if request.method=='POST':
		
		order.delete()
		return redirect('/')
	context={'order':order}
	return render(request,'accounts/delete_order.html',context)
@authenticated_user

def registerPage(request):
	form=CreateUser()
	if request.method=='POST':
		form=CreateUser(request.POST)
		if form.is_valid():
			
			user=form.save()
			username=form.cleaned_data.get('username')
			group=Group.objects.get(name='customer')
			user.groups.add(group)
			Customer.objects.create(user=user,name=username)

			messages.success(request,'Account Created For ' + username)
			return redirect('login')
			
	context={'form':form}
	return render(request, 'accounts/register.html',context)


@authenticated_user
def loginPage(request):
	if request.method=='POST':
		username=request.POST.get('username')
		password=request.POST.get('password')
		user=authenticate(request, username=username, password=password)
		if user is not None:
			login(request,user)
			return redirect('home')
		else:
			messages.info(request, 'Username Or Password is incorrect')
			return redirect('login')
	return render(request, 'accounts/login.html')

def logoutUser(request):
	logout(request)
	return redirect('login')


@login_required(login_url='login')
@allowed_user(allowed_role=['customer'])
def userPage(request):

	orders=request.user.customer.order_set.all()
	total_order=orders.count()
	pending=orders.filter(status='Pending').count()
	delivered=orders.filter(status='Delivered').count()
	context={'Pending':pending,'Delivered':delivered,'Total_order':orders}
	return render(request,'accounts/UserPage.html',context)