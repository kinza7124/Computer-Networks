import socket
import json

def start_client():
    grade_point = float(input("Enter your grade point: "))
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(("127.0.0.1", 6000))

    client_socket.send(str(grade_point).encode())

    response = client_socket.recv(1024).decode()
    result = json.loads(response)

    if "error" in result:
        print(f"Error: {result['error']}")
    else:
        print(f"Letter Grade: {result['letter_grade']}")
        print(f"Qualification: {result['qualification']}")

    client_socket.close()

if __name__ == "__main__":
    start_client()
