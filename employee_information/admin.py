from django.contrib import admin
from employee_information.models import Department, Position, Employees, Customer, CDRLog, Location, Plan,Sale

# Register your models here.
admin.site.register(Department)
admin.site.register(Position)
admin.site.register(Employees)
admin.site.register(Customer)
admin.site.register(CDRLog)
admin.site.register(Location)
admin.site.register(Plan)
admin.site.register(Sale)