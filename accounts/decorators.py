from django.http import HttpResponse
from django.shortcuts import redirect

def authenticated_user(func):
	def wrapper_func(request,*args,**kwargs):
		if request.user.is_authenticated:
			return redirect('home')
		else:
			return func(request,*args,**kwargs)
	return wrapper_func

def allowed_user(allowed_role=[]):
	def decorator(func):
		def wrapper_func(request, *args, **kwargs):
			group=None
			if request.user.groups.exists():
				group=request.user.groups.all()[0].name
			if group in allowed_role:
				return func(request,*args,**kwargs)
			else:
				return HttpResponse("You're not authorized to see this page")
			
		return wrapper_func
	return decorator
def admin_only(func):
	def wrapper_func(request,*args,**kwargs):
		if request.user.groups.exists():
			if request.user.groups.all()[0].name=='admin':
				return func(request,*args,**kwargs)
			return redirect('userpage')
	return wrapper_func