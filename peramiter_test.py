from zk import ZK

def list_methods():
    zk_ip = '192.168.1.5'  # Replace with your ZKTeco machine IP
    port = 4370
    zk = ZK(zk_ip, port=port, timeout=5)
    conn = None
    try:
        # Attempt to connect to the ZKTeco machine
        conn = zk.connect()
        print("Connected to ZKTeco machine.")

        # List available methods
        methods = dir(conn)
        print("Available methods:")
        for method in methods:
            print(method)

    except Exception as e:
        print(f"Error occurred: {e}")
    finally:
        if conn:
            conn.disconnect()
            print("Disconnected from ZKTeco machine.")

list_methods()



from zk import ZK

def list_users():
    zk_ip = '192.168.1.5'  # Replace with your ZKTeco machine IP
    port = 4370
    zk = ZK(zk_ip, port=port, timeout=5)
    conn = None
    try:
        # Attempt to connect to the ZKTeco machine
        conn = zk.connect()
        print("Connected to ZKTeco machine.")

        # Retrieve and print all users
        users = conn.get_users()
        for user in users:
            print(f"User ID: {user.uid}, Name: {user.name}, Badge Number: {user.card}")

    except Exception as e:
        print(f"Error occurred: {e}")
    finally:
        if conn:
            conn.disconnect()
            print("Disconnected from ZKTeco machine.")

list_users()
