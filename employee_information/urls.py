from . import views
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path
from django.views.generic.base import RedirectView

urlpatterns = [
    path('redirect-admin', RedirectView.as_view(url="/admin"),name="redirect-admin"),
    path('', views.home, name="home-page"),
    path('login', auth_views.LoginView.as_view(template_name = 'employee_information/login.html',redirect_authenticated_user=True), name="login"),
    path('userlogin', views.login_user, name="login-user"),
    path('logout', views.logoutuser, name="logout"),
    path('about', views.about, name="about-page"),
    path('departments', views.departments, name="department-page"),
    path('manage_departments', views.manage_departments, name="manage_departments-page"),
    path('save_department', views.save_department, name="save-department-page"),
    path('delete_department', views.delete_department, name="delete-department"),
    path('positions', views.positions, name="position-page"),
    path('manage_positions', views.manage_positions, name="manage_positions-page"),
    path('save_position', views.save_position, name="save-position-page"),
    path('delete_position', views.delete_position, name="delete-position"),
    path('customer', views.customers, name="customer-page"),
    path('manage_customer', views.manage_customer, name="manage_customers-page"),
    path('save_customers', views.save_customer, name="save-customer-page"),
    path('delete_customer', views.delete_customer, name="delete-customer"),
    path('employees', views.employees, name="employee-page"),
    path('manage_employees', views.manage_employees, name="manage_employees-page"),
    path('save_employee', views.save_employee, name="save-employee-page"),
    path('delete_employee', views.delete_employee, name="delete-employee"),
    path('view_employee', views.view_employee, name="view-employee-page"),

    path('cdrlog', views.cdrlogs, name="cdrlog-page"),
    path('manage_cdrlog', views.manage_cdrlog, name="manage_cdrlog-page"),
    path('save_cdrlog', views.save_cdrlog, name="save-cdrlog-page"),
    #path('manage_cdrlog/<int:id>/', views.manage_cdrlog, name='manage-cdrlog-page'),
    path('delete_cdrlog', views.delete_cdrlog, name="delete-cdrlog"),
    path('view_cdrlog', views.view_cdrlog, name="view-cdrlog-page"),

    path('location', views.locations, name="location-page"),
    path('manage_location', views.manage_location, name="manage_locations-page"),
    path('save_location', views.save_location, name="save-location-page"),
    path('delete_location', views.delete_location, name="delete-location"),
    
    path('plans', views.plans, name="plan-page"),
    path('manage_plans', views.manage_plan, name="manage_plans-page"),
    path('save_plans', views.save_plan, name="save-plan-page"),
    path('delete_plan', views.delete_plan, name="delete-plan"),
    
     path('Sales', views.sales, name="sale-page"),
    path('manage_sales', views.manage_sales, name="manage_sales-page"),
    path('save_sales', views.save_sale, name="save-sale-page"),
    path('delete_sale', views.delete_sale, name="delete-sale"),
    path('view_sales', views.view_sale, name="view-sales-page"),
]