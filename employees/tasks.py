# employees/tasks.py
from .models import Employee
from datetime import date
from zk import ZK

# Function to remove expired employees from the ZKTeco machine
def remove_employee_from_zkteco(employee):
    zk = ZK('192.168.1.5', port=4370, timeout=5)
    conn = None
    try:
        conn = zk.connect()
        conn.disable_device()
        conn.delete_user(int(employee.rfid_card))
        conn.enable_device()
        employee.added_to_machine = False
        employee.is_active = False
        employee.save()
    except Exception as e:
        print(f"Error removing user {employee.name}: {e}")
    finally:
        if conn:
            conn.disconnect()

# Task to check for expired employees
def check_and_remove_expired_employees():
    expired_employees = Employee.objects.filter(expire_date__lt=date.today(), is_active=True)
    for employee in expired_employees:
        remove_employee_from_zkteco(employee)
