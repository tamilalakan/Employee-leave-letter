from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from account.models import Employee


class CreateUserForm(UserCreationForm):
	class Meta:
		model = User
		fields = ['username','email','password1','password2']

class EmployeeList(forms.ModelForm):
	class Meta:
		model = Employee
		fields = ['username','email','password1','password2']
