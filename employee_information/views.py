from django.shortcuts import redirect, render
from employee_information.models import Department, Position, Employees, Customer, CDRLog, Location, Plan, Sale
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, JsonResponse
from django.shortcuts import  get_object_or_404
import json
import logging



#from django.db.models import Q
employees = [

    {
        'code':1,
        'name':"John D Smith",
        'contact':'09123456789',
        'address':'Sample Address only'
    },{
        'code':2,
        'name':"Claire C Blake",
        'contact':'09456123789',
        'address':'Sample Address2 only'
    }

]
# Login
def login_user(request):
    logout(request)
    resp = {"status":'failed','msg':''}
    username = ''
    password = ''
    if request.POST:
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                resp['status']='success'
            else:
                resp['msg'] = "Incorrect username or password"
        else:
            resp['msg'] = "Incorrect username or password"
    return HttpResponse(json.dumps(resp),content_type='application/json')

#Logout
def logoutuser(request):
    logout(request)
    return redirect('/')

# Create your views here.
@login_required
def home(request):
    context = {
        'page_title':'Home',
        'employees':employees,
        'total_department':len(Department.objects.all()),
        'total_position':len(Position.objects.all()),
        'total_employee':len(Employees.objects.all()),
    }
    return render(request, 'employee_information/home.html',context)


def about(request):
    context = {
        'page_title':'About',
    }
    return render(request, 'employee_information/about.html',context)

# Departments
@login_required
def departments(request):
    department_list = Department.objects.all()
    context = {
        'page_title':'Departments',
        'departments':department_list,
    }
    return render(request, 'employee_information/departments.html',context)
@login_required
def manage_departments(request):
    department = {}
    if request.method == 'GET':
        data =  request.GET
        id = ''
        if 'id' in data:
            id= data['id']
        if id.isnumeric() and int(id) > 0:
            department = Department.objects.filter(id=id).first()
    
    context = {
        'department' : department
    }
    return render(request, 'employee_information/manage_department.html',context)

@login_required
def save_department(request):
    data =  request.POST
    resp = {'status':'failed'}
    try:
        if (data['id']).isnumeric() and int(data['id']) > 0 :
            save_department = Department.objects.filter(id = data['id']).update(name=data['name'], description = data['description'],status = data['status'])
        else:
            save_department = Department(name=data['name'], description = data['description'],status = data['status'])
            save_department.save()
        resp['status'] = 'success'
    except:
        resp['status'] = 'failed'
    return HttpResponse(json.dumps(resp), content_type="application/json")

@login_required
def delete_department(request):
    data =  request.POST
    resp = {'status':''}
    try:
        Department.objects.filter(id = data['id']).delete()
        resp['status'] = 'success'
    except:
        resp['status'] = 'failed'
    return HttpResponse(json.dumps(resp), content_type="application/json")

# Positions
@login_required
def positions(request):
    position_list = Position.objects.all()
    context = {
        'page_title':'Positions',
        'positions':position_list,
    }
    return render(request, 'employee_information/positions.html',context)
@login_required
def manage_positions(request):
    position = {}
    if request.method == 'GET':
        data =  request.GET
        id = ''
        if 'id' in data:
            id= data['id']
        if id.isnumeric() and int(id) > 0:
            position = Position.objects.filter(id=id).first()
    
    context = {
        'position' : position
    }
    return render(request, 'employee_information/manage_position.html',context)

@login_required
def save_position(request):
    data =  request.POST
    resp = {'status':'failed'}
    try:
        if (data['id']).isnumeric() and int(data['id']) > 0 :
            save_position = Position.objects.filter(id = data['id']).update(name=data['name'], description = data['description'],status = data['status'])
        else:
            save_position = Position(name=data['name'], description = data['description'],status = data['status'])
            save_position.save()
        resp['status'] = 'success'
    except:
        resp['status'] = 'failed'
    return HttpResponse(json.dumps(resp), content_type="application/json")

@login_required
def delete_position(request):
    data =  request.POST
    resp = {'status':''}
    try:
        Position.objects.filter(id = data['id']).delete()
        resp['status'] = 'success'
    except:
        resp['status'] = 'failed'
    return HttpResponse(json.dumps(resp), content_type="application/json")

@login_required
# Employees
def employees(request):
    employee_list = Employees.objects.all()
    context = {
        'page_title':'Employees',
        'employees':employee_list,
    }
    return render(request, 'employee_information/employees.html',context)
@login_required
def manage_employees(request):
    employee = {}
    departments = Department.objects.filter(status = 1).all() 
    positions = Position.objects.filter(status = 1).all() 
    if request.method == 'GET':
        data =  request.GET
        id = ''
        if 'id' in data:
            id= data['id']
        if id.isnumeric() and int(id) > 0:
            employee = Employees.objects.filter(id=id).first()
    context = {
        'employee' : employee,
        'departments' : departments,
        'positions' : positions
    }
    return render(request, 'employee_information/manage_employee.html',context)

@login_required
def save_employee(request):
    data =  request.POST
    resp = {'status':'failed'}
    if (data['id']).isnumeric() and int(data['id']) > 0:
        check  = Employees.objects.exclude(id = data['id']).filter(code = data['code'])
    else:
        check  = Employees.objects.filter(code = data['code'])

    if len(check) > 0:
        resp['status'] = 'failed'
        resp['msg'] = 'Code Already Exists'
    else:
        try:
            dept = Department.objects.filter(id=data['department_id']).first()
            pos = Position.objects.filter(id=data['position_id']).first()
            if (data['id']).isnumeric() and int(data['id']) > 0 :
                save_employee = Employees.objects.filter(id = data['id']).update(code=data['code'], firstname = data['firstname'],middlename = data['middlename'],lastname = data['lastname'],dob = data['dob'],gender = data['gender'],contact = data['contact'],email = data['email'],address = data['address'],department_id = dept,position_id = pos,date_hired = data['date_hired'],salary = data['salary'],status = data['status'])
            else:
                save_employee = Employees(code=data['code'], firstname = data['firstname'],middlename = data['middlename'],lastname = data['lastname'],dob = data['dob'],gender = data['gender'],contact = data['contact'],email = data['email'],address = data['address'],department_id = dept,position_id = pos,date_hired = data['date_hired'],salary = data['salary'],status = data['status'])
                save_employee.save()
            resp['status'] = 'success'
        except Exception:
            resp['status'] = 'failed'
            print(Exception)
            print(json.dumps({"code":data['code'], "firstname" : data['firstname'],"middlename" : data['middlename'],"lastname" : data['lastname'],"dob" : data['dob'],"gender" : data['gender'],"contact" : data['contact'],"email" : data['email'],"address" : data['address'],"department_id" : data['department_id'],"position_id" : data['position_id'],"date_hired" : data['date_hired'],"salary" : data['salary'],"status" : data['status']}))
    return HttpResponse(json.dumps(resp), content_type="application/json")

@login_required
def delete_employee(request):
    data =  request.POST
    resp = {'status':''}
    try:
        Employees.objects.filter(id = data['id']).delete()
        resp['status'] = 'success'
    except:
        resp['status'] = 'failed'
    return HttpResponse(json.dumps(resp), content_type="application/json")

@login_required
def view_employee(request):
    employee = {}
    departments = Department.objects.filter(status = 1).all() 
    positions = Position.objects.filter(status = 1).all() 
    if request.method == 'GET':
        data =  request.GET
        id = ''
        if 'id' in data:
            id= data['id']
        if id.isnumeric() and int(id) > 0:
            employee = Employees.objects.filter(id=id).first()
    context = {
        'employee' : employee,
        'departments' : departments,
        'positions' : positions
    }
    return render(request, 'employee_information/view_employee.html',context)

#Customer

#@login_required
# customer
@login_required
def customers(request):
    customer_list = Customer.objects.all()
    context = {
        'page_title':'Customers',
        'customers':customer_list,
    }
    return render(request, 'employee_information/customer.html',context)
@login_required
def manage_customer(request):
    customer = {}
    if request.method == 'GET':
        data =  request.GET
        customer_id = ''
        if 'customer_id' in data:
            customer_id= data['customer_id']
        if customer_id.isnumeric() and int(customer_id) > 0:
            customer = Customer.objects.filter(customer_id=customer_id).first()
    
    context = {
        'customer' : customer
    }
    return render(request, 'employee_information/manage_customer.html',context)

@login_required
def save_customer(request):
    data =  request.POST
    resp = {'status':'failed'}
    try:
        if (data['customer_id']).isnumeric() and int(data['customer_id']) > 0 :
            save_customer = Customer.objects.filter(customer_id = data['customer_id']).update(name=data['name'],address = data['address'],email = data['email'],phone = data['phone'], locationid = data['locationid'])
        else:
            save_customer = Customer(name=data['name'], address = data['address'],email = data['email'],phone = data['phone'], locationid = data['locationid'])
            save_customer.save()
        resp['status'] = 'success'
    except:
        resp['status'] = 'failed'
    return HttpResponse(json.dumps(resp), content_type="application/json")

@login_required
def delete_customer(request):
    data =  request.POST
    resp = {'status':''}
    try:
        Customer.objects.filter(customer_id = data['customer_id']).delete()
        resp['status'] = 'success'
    except:
        resp['status'] = 'failed'
    return HttpResponse(json.dumps(resp), content_type="application/json")

# Plan
@login_required
def plans(request):
    plan_list = Plan.objects.all()
    context = {
        'page_title':'Plans',
        'plans':plan_list,
    }
    return render(request, 'employee_information/plan.html',context)
@login_required
def manage_plan(request):
    plan= {}
    if request.method == 'GET':
        data =  request.GET
        id = ''
        if 'id' in data:
            id= data['id']
        if id.isnumeric() and int(id) > 0:
            position = Plan.objects.filter(id=id).first()
    
    context = {
        'plan' : plan
    }
    return render(request, 'employee_information/manage_plan.html',context)

@login_required
def save_plan(request):
    data =  request.POST
    resp = {'status':'failed'}
    try:
        if (data['id']).isnumeric() and int(data['id']) > 0 :
            save_plan = Plan.objects.filter(id = data['id']).update(name=data['name'],  data_limit = data[' data_limit '], talk_time_limit = data[' talk_time_limit '], sms_limit = data['sms_limit'], place = data['place'], status = data['status'])
        else:
            save_plan = Plan(name=data['name'], data_limit = data['data_limit'],talk_time_limit = data['talk_time_limit'], sms_limit = data['sms_limit'], place = data['place'], status = data['status'])
            save_plan.save()
        resp['status'] = 'success'
    except:
        resp['status'] = 'failed'
    return HttpResponse(json.dumps(resp), content_type="application/json")

@login_required
def delete_plan(request):
    data =  request.POST
    resp = {'status':''}
    try:
        Plan.objects.filter(id = data['id']).delete()
        resp['status'] = 'success'
    except:
        resp['status'] = 'failed'
    return HttpResponse(json.dumps(resp), content_type="application/json")

#Location

# location
@login_required
def locations(request):
    location_list = Location.objects.all()
    context = {
        'page_title':'Locations',
        'locations':location_list,
    }
    return render(request, 'employee_information/location.html',context)
@login_required
def manage_location(request):
    location = {}
    if request.method == 'GET':
        data =  request.GET
        locationid = ''
        if 'locationid' in data:
            locationid= data['locationid']
        if locationid.isnumeric() and int(locationid) > 0:
            location= Location.objects.filter(locationid=locationid).first()
    
    context = {
        'location' : location
    }
    return render(request, 'employee_information/manage_location.html',context)

@login_required
def save_location(request):
    data =  request.POST
    resp = {'status':'failed'}
    try:
        if (data['locationid']).isnumeric() and int(data['locationid']) > 0 :
            save_location = Location.objects.filter(locationid = data['locationid']).update(region=data['region'],zone = data['zone'],district = data['district'],sector = data['sector'], cells = data['cells'], village = data['village'], sitename = data['sitename'], sitetechnology = data['sitetechnology'], cellid = data['cellid'])
        else:
            save_location = Location(region=data['region'],zone = data['zone'],district = data['district'],sector = data['sector'], cells = data['cells'], village = data['village'], sitename = data['sitename'], sitetechnology = data['sitetechnology'], cellid = data['cellid'])
            save_location.save()
        resp['status'] = 'success'
    except:
        resp['status'] = 'failed'
    return HttpResponse(json.dumps(resp), content_type="application/json")

@login_required
def delete_location(request):
    data =  request.POST
    resp = {'status':''}
    try:
        Location.objects.filter(locationid = data['locationid']).delete()
        resp['status'] = 'success'
    except:
        resp['status'] = 'failed'
    return HttpResponse(json.dumps(resp), content_type="application/json")


#CDR

# Import necessary modules


# CDR_LOGS
@login_required
def cdrlogs(request):
    cdrlog_list = CDRLog.objects.all()
    context = {
        'page_title': 'cdrlogs',
        'cdrlog': cdrlog_list,
    }
    return render(request, 'employee_information/cdr_log.html', context)

@login_required
def manage_cdrlog(request):
    logger = logging.getLogger(__name__)  # Define logger here
    cdrlog = {}
    customers = Customer.objects.all()
    if request.method == 'GET':
        data = request.GET
        id = ''
        if 'id' in data:
            id = data['id']
        if id.isnumeric() and int(id) > 0:
            cdrlog = CDRLog.objects.filter(id=id).first()
    context = {
        'cdrlog': cdrlog,
        'customers': customers,
    }
    return render(request, 'employee_information/manage_cdr.html', context)

@login_required
def save_cdrlog(request):
    logger = logging.getLogger(__name__)  # Define logger here
    data = request.POST
    resp = {'status': 'failed'}
    try:
        cust = Customer.objects.filter(id=data['customer_id']).first()
        if data['id'].isnumeric() and int(data['id']) > 0:
            save_cdrlog = CDRLog.objects.filter(id=data['id']).update(
                code=data['code'],
                customer_name=cust,
                call_duration=data['call_duration'],
                MSISDN=data['MSISDN'],
                status=data['status']
            )
        else:
            save_cdrlog = CDRLog(
                code=data['code'],
                customer_name=cust,
                call_duration=data['call_duration'],
                MSISDN=data['MSISDN'],
                status=data['status']
            )
            save_cdrlog.save()
            resp['status'] = 'success'
    except Exception as e:
        logger.error(f"An error occurred: {str(e)}")
    return HttpResponse(json.dumps(resp), content_type="application/json")

@login_required
def delete_cdrlog(request):
    data = request.POST
    resp = {'status': ''}
    try:
        CDRLog.objects.filter(id=data['id']).delete()
        resp['status'] = 'success'
    except:
        resp['status'] = 'failed'
    return HttpResponse(json.dumps(resp), content_type="application/json")

@login_required
def view_cdrlog(request):
    cdrlog = {}
    customers = Customer.objects.filter(status=1).all()

    if request.method == 'GET':
        data = request.GET
        id = ''
        if 'id' in data:
            id = data['id']
        if id.isnumeric() and int(id) > 0:
            cdrlog = CDRLog.objects.filter(id=id).first()
    context = {
        'cdrlog': cdrlog,
        'customers': customers,
    }
    return render(request, 'employee_information/view_cdrlog.html', context)






@login_required
# Sales
def sales(request):
    sale_list = Sale.objects.all()
    context = {
        'page_title':'Sales',
        'sales':sale_list,
    }
    return render(request, 'employee_information/sales.html',context)
@login_required
def manage_sales(request):
    sale = {}
    employees = Employees.objects.filter(status = 1).all() 
    customers = Customer.objects.all()
    plans = Plan.objects.filter(status = 1).all() 
    if request.method == 'GET':
        data =  request.GET
        id = ''
        if 'id' in data:
            id= data['id']
        if id.isnumeric() and int(id) > 0:
            sale= Sale.objects.filter(id=id).first()
    context = {
        'sale' : sale,
        'employee' : employees,
        'customer' : customers,
        'plan' : plans
    }
    return render(request, 'employee_information/manage_sales.html',context)

@login_required
def save_sale(request):
    data =  request.POST
    resp = {'status':'failed'}
    if (data['id']).isnumeric() and int(data['id']) > 0:
        check  = Sale.objects.exclude(id = data['id']).filter(code = data['code'])
    else:
        check  = Sale.objects.filter(code = data['code'])

    if len(check) > 0:
        resp['status'] = 'failed'
        resp['msg'] = 'Code Already Exists'
    else:
        try:
            emp = Employees.objects.filter(id=data['employee_id']).first()
            cust = Customer.objects.filter(id=data['customer_id']).first()
            pla = Plan.objects.filter(id=data['plan_id']).first()
            if (data['id']).isnumeric() and int(data['id']) > 0 :
                save_sale = Sale.objects.filter(id = data['id']).update(code=data['code'],employee_id = emp,customer_id = cust,plan_id = pla,sale = data['sale_date'],status = data['status'])
            else:
                save_sale= Sale(code=data['code'],employee_id = emp,customer_id = cust,plan_id = pla,sale = data['sale_date'],status = data['status'])
                save_sale.save()
            resp['status'] = 'success'
        except Exception:
            resp['status'] = 'failed'
            print(Exception)
            print(json.dumps({"code":data['code'], "employee_id" : data['employee_id'],"customer_id" : data['customer_id'], "plan_id" : data['plan_id'],"sale_date" : data['sale_date'],"status" : data['status']}))
    return HttpResponse(json.dumps(resp), content_type="application/json")

@login_required
def delete_sale(request):
    data =  request.POST
    resp = {'status':''}
    try:
        Sale.objects.filter(id = data['id']).delete()
        resp['status'] = 'success'
    except:
        resp['status'] = 'failed'
    return HttpResponse(json.dumps(resp), content_type="application/json")

@login_required
def view_sale(request):
    sale = {}
    employees = Employees.objects.filter(status = 1).all() 
    customers = Customer.objects.all() 
    plans= Plan.objects.filter(status = 1).all() 
    
    if request.method == 'GET':
        data =  request.GET
        id = ''
        if 'id' in data:
            id= data['id']
        if id.isnumeric() and int(id) > 0:
            sale = Sale.objects.filter(id=id).first()
    context = {
        'sale' : sale,
        'employee' : employees,
        'customers' : customers,
         'plans' : plans

    }
    return render(request, 'employee_information/view_sales.html',context)










