from django.contrib import admin
from account.models import Employee
# Register your models here.
admin.site.register(Employee)
from django.contrib.admin.models import LogEntry
LogEntry.objects.all().delete()
