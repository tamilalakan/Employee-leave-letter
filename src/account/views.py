from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from account.forms import CreateUserForm
from django.contrib import messages 
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.sessions.models import Session

# Create your views here.

from account.forms import EmployeeList
from account.models import Employee
import datetime
from datetime import date
from django.http import HttpResponse, HttpResponseRedirect


def home(request):
	# if request.user:
	# 	to_day = str(datetime.date.today())
	# 	to_day = datetime.datetime.strptime(to_day, '%Y-%m-%d')
	# 	obj = Employee.objects.all()
	# 	for i in obj:
	# 		if i.start_date and i.last_date:
	# 			s = str(i.last_date)
				
	# 			last = datetime.datetime.strptime(s, '%Y-%m-%d')
	# 			if ((last - to_day).days) < 0:
	# 				i.start_date = None
	# 				i.last_date = None
	# 				i.description = None
	# 				i.approve = None
	# 				i.save()
	return render(request,'account/home.html')


def register(request):
	if request.method == "POST":
		form = CreateUserForm(request.POST)

		employee = EmployeeList(request.POST)

		if form.is_valid() and employee.is_valid():
			form.save()
			employee.save()	
			username = employee.cleaned_data.get('username')
			raw_password = employee.cleaned_data.get('password1')

			user = authenticate(request, username=username, password=raw_password)
			if user is not None:
				login(request, user)
				return redirect('home')


	else:
		form = CreateUserForm()
		employee = EmployeeList()
	return render(request,"account/register.html",{"form":form})

def loginPage(request):
	if request.method == "POST":
		username = request.POST.get('username')
		password = request.POST.get('password')
		employee = Employee.objects.all()


		user = authenticate(request, username=username,password=password)
		print(user)
		if user is not None:
			login(request,user)
			if user.is_staff:
				print("Success tamil..keep moving..")
				return redirect('home')
			else:
				return redirect('home')
		else:
			messages.info(request,"*Username or Password is incorrect")
	return render(request,"account/login.html")

def logoutPage(request):
	logout(request)
	return redirect('home')


def letter(request):
	context = {}
	
	nam = request.user.username
	obj = Employee.objects.get(username=nam)
	import time

	if request.method == "POST":
		context = {}

		nam = request.user.username
		obj = Employee.objects.get(username=nam)
		
		start = request.POST.get('start_date')
		last = request.POST.get('last_date')
		des = request.POST.get('description')
	
		des = des.split(' ')
		a = []
		s = 8
		for i in range(len(des)):
			if i == s:
				a.append('\n')
				s+=8
			else:
				a.append(des[i])
				a.append(' ')
		des = ''.join(a)

		obj.start_date = start
		obj.last_date = last
		obj.description = des
		
		start = datetime.datetime.strptime(start, '%Y-%m-%d')
		last = datetime.datetime.strptime(last, '%Y-%m-%d')

		day = abs(start - last)
		
		obj.leave = (obj.leave) - ((day.days) + 1)
		
		
		obj.save()

	
		time.sleep(5)
		return redirect('home')

	return render(request,"account/letter.html",{'ob':obj.leave,'description':obj.description, 'approve':obj.approve, 'leave':obj.leave})



def approve(request):
	details = Employee.objects.all()
	for obj in details:
		if ('approved'+str(obj.id)) in request.POST:
			obj.approve = "Approved"
			obj.save()
			break
		elif ('reject'+str(obj.id)) in request.POST:
			obj.approve = "Rejected"
			obj.save()
			break

	return render(request,'account/approve.html',{"details":details})