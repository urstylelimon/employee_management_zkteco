from zk import ZK


def test_zkteco_connection():
    zk_ip = '192.168.1.5'  # Replace with your ZKTeco machine IP
    port = 4370
    zk = ZK(zk_ip, port=port, timeout=5)
    conn = None
    try:
        # Attempt to connect to the ZKTeco machine
        conn = zk.connect()
        print("Connected to ZKTeco machine.")

        # Check if the device is connected and available
        if conn:
            print("Device is connected.")
        else:
            print("Failed to connect to device.")

    except Exception as e:
        print(f"Error occurred: {e}")

    finally:
        if conn:
            conn.disconnect()
            print("Disconnected from ZKTeco machine.")


# Run the test
test_zkteco_connection()
