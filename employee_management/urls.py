# employee_management/urls.py
from django.contrib import admin
from django.urls import path
from employees import views as employee_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('employees/new/', employee_views.employee_create_view, name='employee_create'),
    path('employees/', employee_views.employee_list_view, name='employee_list'),
    path('user-list/', employee_views.user_list_view, name='user_list'),
]
