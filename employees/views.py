# employees/views.py
from django.shortcuts import render, redirect
from .models import Employee
from .forms import EmployeeForm
from zk import ZK

def add_employee_to_zkteco(employee):
    zk_ip = '192.168.1.5'  # Replace with your ZKTeco machine IP
    port = 4370
    zk = ZK(zk_ip, port=port, timeout=5)
    conn = None
    try:
        # Attempt to connect to the ZKTeco machine
        conn = zk.connect()
        print("Connected to ZKTeco machine.")

        # Disable the device to ensure data consistency
        conn.disable_device()
        print("Device disabled.")

        # Convert RFID card number to integer
        try:
            rfid_card_number = int(employee.rfid_card)
        except ValueError:
            raise ValueError("Invalid RFID card number format.")

        # Ensure the RFID card number is within the 32-bit range
        if not (0 <= rfid_card_number <= 4294967295):
            raise ValueError("RFID card number is out of 32-bit range.")

        # Convert RFID card number to Badge Number if needed
        # Placeholder for conversion logic if different format is needed
        badge_number = rfid_card_number  # Adjust this based on your Badge Number format

        print(f"Setting user with Badge Number: {badge_number}")
        uid = 0
        users = conn.get_users()
        if users:
            for user in users:
                id = user.uid
            uid = id + 1

        else:
            uid = 1

        # Set user data on the ZKTeco machine
        conn.set_user(uid= uid ,card=badge_number, name=employee.name)
        print(f"User {employee.name} added.")

        # Re-enable the device
        conn.enable_device()
        print("Device enabled.")

        # Mark the employee as added to the machine
        employee.added_to_machine = True
        employee.save()
        print(f"Employee {employee.name} saved successfully.")

    except Exception as e:
        print(f"Error occurred: {e}")
    finally:
        if conn:
            conn.disconnect()
            print("Disconnected from ZKTeco machine.")



# View to handle employee form submission
def employee_create_view(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            employee = form.save(commit=False)
            employee.save()
            add_employee_to_zkteco(employee)
            return redirect('employee_list')
    else:
        form = EmployeeForm()
    return render(request, 'employees/employee_form.html', {'form': form})

# View to display employee list
def employee_list_view(request):
    employees = Employee.objects.all()
    return render(request, 'employees/employee_list.html', {'employees': employees})


def user_list_view(request):
    users = []

    zk_ip = '192.168.1.5'  # Replace with your ZKTeco machine IP
    port = 4370
    zk = ZK(zk_ip, port=port, timeout=5)
    conn = None
    try:
        # Attempt to connect to the ZKTeco machine
        conn = zk.connect()
        print("Connected to ZKTeco machine.")

        # Disable the device to ensure data consistency
        conn.disable_device()
        print("Device disabled.")

        # Fetch the user data
        zk_users = conn.get_users()
        if zk_users:
            for user in zk_users:
                users.append({'id':user.uid,'Badge_Number': user.card, 'name': user.name})
        else:
            print("No users found on ZKTeco device.")

        # Re-enable the device
        conn.enable_device()
        print("Device enabled.")

    except Exception as e:
        print(f"Error occurred: {e}")
    finally:
        if conn:
            conn.disconnect()
            print("Disconnected from ZKTeco machine.")

    return render(request, 'employees/user_list.html', {'users': users})
