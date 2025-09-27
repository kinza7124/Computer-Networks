import socket
import json

def start_client():
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    operation = input("Enter operation (+, -, *, /): ")
    request = {
        "num1": num1,
        "num2": num2,
        "operation": operation
    }
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(("127.0.0.1", 5555))

    client_socket.send(json.dumps(request).encode())

    response = client_socket.recv(1024).decode()
    result = json.loads(response).get("result", "Error")

    print(f"Result: {result}")
    
    client_socket.close()

if __name__ == "__main__":
    start_client()
