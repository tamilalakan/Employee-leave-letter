from django.db import models

# Create your models here.

class Employee(models.Model):
	username = models.CharField(max_length=32)
	email = models.EmailField()
	password1 = models.CharField(max_length=20)
	password2 = models.CharField(max_length=20)
	leave = models.IntegerField(blank=True,default=4)
	start_date = models.DateField(blank=True,null=True)
	last_date = models.DateField(blank=True,null=True)
	description = models.TextField(blank=True, null=True)
	approve = models.CharField(max_length=10,blank=True, null=True)



	def __str__(self):
		return self.username

