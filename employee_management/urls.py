# employee_management/urls.py
from django.contrib import admin
from django.urls import path
from employees import views as employee_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',employee_views.home_page,name='home'),
    path('employees/new/', employee_views.employee_create_view, name='employee_create'),
    path('employees/', employee_views.employee_list_view, name='employee_list'),
    path('user_list/', employee_views.user_list_view, name='user_list'),
    path('employee/<str:pk>', employee_views.single_user, name='single_user'),
    path('employee/<int:pk>/toggle-status/', employee_views.toggle_employee_status, name='toggle_employee_status'),

]
