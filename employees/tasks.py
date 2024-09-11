# employees/tasks.py
from .models import Employee
from datetime import date
from zk import ZK

def remove_employee_from_zkteco(employee):
    zk = ZK('192.168.1.5', port=4370, timeout=5)
    conn = None
    try:
        conn = zk.connect()
        conn.disable_device()

        # Convert RFID card to 32-bit integer if necessary
        rfid_number = int(employee.uid)

        # Ensure the number is within valid 32-bit range
        if rfid_number > 4294967295 or rfid_number < 0:
            raise ValueError(f"RFID number {rfid_number} is out of the 32-bit range")

        # Delete the user from the ZKTeco machine
        conn.delete_user(uid=employee.uid)  # Ensure correct format for delete_user
        print(f" Successfully Deleted {employee.name}")
        conn.enable_device()

    except Exception as e:
        print(f"Error removing user {employee.name}: {e}")
    finally:
        if conn:
            conn.disconnect()





# Task to check for expired employees

def check_and_remove_expired_employees():
    zk = ZK('192.168.1.5', port=4370, timeout=5)
    conn = None
    try:
        conn = zk.connect()
        print("Connect Successfully")
        conn.disable_device()
        machine_users = conn.get_users()
        conn.enable_device()


        # Remove expired employees from the machine
        for user in machine_users:
            print(user.name, user.card)
            object1 = Employee.objects.get(name=user.name)
            print(object1.name, object1.rfid_card)

            if object1.expire_date >= date.today():
                print("Find one person",object1.name)
                object1.is_active = False
                object1.save()
                remove_employee_from_zkteco(user)
            else:
                print("No one still Expired Now")



    except Exception as e:
        print(f"Error during synchronization: {e}")
    finally:
        if conn:
            conn.disconnect()
