from datetime import datetime
from django.db import models
from django.utils import timezone

# Create your models here.
class Department(models.Model):
    name = models.TextField() 
    description = models.TextField() 
    status = models.IntegerField() 
    date_added = models.DateTimeField(default=timezone.now) 
    date_updated = models.DateTimeField(auto_now=True) 

    def __str__(self):
        return self.name

class Position(models.Model):
    name = models.TextField() 
    description = models.TextField() 
    status = models.IntegerField() 
    date_added = models.DateTimeField(default=timezone.now) 
    date_updated = models.DateTimeField(auto_now=True) 

    def __str__(self):
        return self.name


class Employees(models.Model):
    code = models.CharField(max_length=100,blank=True) 
    firstname = models.TextField() 
    middlename = models.TextField(blank=True,null= True) 
    lastname = models.TextField() 
    gender = models.TextField(blank=True,null= True) 
    dob = models.DateField(blank=True,null= True) 
    contact = models.TextField() 
    address = models.TextField() 
    email = models.TextField() 
    department_id = models.ForeignKey(Department, on_delete=models.CASCADE) 
    position_id = models.ForeignKey(Position, on_delete=models.CASCADE) 
    date_hired = models.DateField() 
    salary = models.FloatField(default=0) 
    status = models.IntegerField() 
    date_added = models.DateTimeField(default=timezone.now) 
    date_updated = models.DateTimeField(auto_now=True) 

    def __str__(self):
        return self.firstname + ' ' +self.middlename + ' '+self.lastname + ' '
    
class Customer(models.Model):
    customer_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    locationid = models.IntegerField(null=True, blank=True)
    def __str__(self):
        return self.name
    
#CDR_LOGS
class CDRLog(models.Model) :
    code = models.CharField(max_length=100,blank=True) 
    customer_id = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True)
    call_duration = models.IntegerField()
    MSISDN  = models.CharField(max_length=20)
    call_date = models.DateField()
    status = models.IntegerField( default=1) 

class Location(models.Model):
    locationid = models.IntegerField(primary_key=True)
    region = models.CharField(max_length=50, null=True)
    zone = models.CharField(max_length=50, null=True)
    district = models.CharField(max_length=50, null=True)
    sector = models.CharField(max_length=50, null=True)
    cells = models.CharField(max_length=50, null=True)
    village = models.CharField(max_length=50, null=True)
    sitename = models.CharField(max_length=50, null=True)
    sitetechnology = models.CharField(max_length=50, null=True)
    cellid = models.IntegerField(null=True)

class Plan(models.Model):
    name = models.CharField(max_length=100)
    data_limit = models.IntegerField()
    talk_time_limit = models.IntegerField()
    sms_limit = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.IntegerField() 

    def __str__(self):
        return self.name

class Sale(models.Model):
    code = models.CharField(max_length=100,blank=True)
    employee_id = models.ForeignKey(Employees,  on_delete=models.CASCADE)
    customer_id = models.ForeignKey(Customer,  on_delete=models.CASCADE)
    plan_id = models.ForeignKey(Plan,  on_delete=models.CASCADE)
    sale_date = models.DateField()
    amount = models.IntegerField()
    status = models.IntegerField() 