from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Customer(models.Model):
	user=models.OneToOneField(User,null=True,on_delete=models.CASCADE )
	name=models.CharField(null=True, max_length=200)
	email=models.CharField(null=True, max_length=200)
	phone_number=models.CharField(null=True, max_length=200)
	date_created=models.DateTimeField(auto_now_add=True)
	def __str__(self):
		return self.name
	def count_order(self):
		return Order.objects.filter(customer=self).count()

class Tag(models.Model):
	TAG=(
		('Sports','Sports'),
		('Summer','Summer'),
		('Kitchen','Kitchen')
		)
	name=models.CharField(choices=TAG,max_length=100)
	def __str__(self):
		return self.name
class Product(models.Model):
	categories=(
		('Outdoor','Outdoor'),
		('Indoor','Indoor')
)
	name=models.CharField(null=True, max_length=200)
	price=models.FloatField()
	category=models.CharField(max_length=100,choices=categories)
	description=models.CharField(null=True,blank=True, max_length=200)
	date_created=models.DateTimeField(auto_now_add=True)
	tag=models.ManyToManyField(Tag)
	def __str__(self):
		return self.name
class Order(models.Model):
	status=(
		('Pending','Pending'),
		('Out For Delivery','Out For Delivery'),
		('Delivered','Delivered')
		)
	customer=models.ForeignKey(Customer,null=True,on_delete=models.SET_NULL)
	product=models.ForeignKey(Product,null=True,on_delete=models.SET_NULL)
	date_created=models.DateTimeField(auto_now_add=True)
	status=models.CharField(max_length=100,choices=status)
	def __str__(self):
		return f'{self.product} {self.status}'
	