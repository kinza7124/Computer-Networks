import socket
import json
import os
FILE_NAME = "calculations.json"

if not os.path.exists(FILE_NAME):
    with open(FILE_NAME, "w") as f:
        json.dump([], f)

def save_to_json(data):
    with open(FILE_NAME, "r") as f:
        history = json.load(f)
    history.append(data)
    with open(FILE_NAME, "w") as f:
        json.dump(history, f, indent=4)

def calculate(num1, num2, operation):
    try:
        if operation == '+':
            return num1 + num2
        elif operation == '-':
            return num1 - num2
        elif operation == '*':
            return num1 * num2
        elif operation == '/':
            return num1 / num2 if num2 != 0 else "Error: Division by zero"
        else:
            return "Error: Invalid operation"
    except Exception as e:
        return f"Error: {e}"

def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(("127.0.0.1", 5555)) 
    server_socket.listen(5)

    print("Server started. Waiting for clients...")

    while True:
        client_socket, address = server_socket.accept()
        print(f"Connection from {address}")
        data = client_socket.recv(1024).decode()
        if not data:
            client_socket.close()
            continue

        try:
            request = json.loads(data)
            num1 = request["num1"]
            num2 = request["num2"]
            operation = request["operation"]
            result = calculate(num1, num2, operation)
            save_to_json({
                "num1": num1,
                "num2": num2,
                "operation": operation,
                "result": result
            })

            response = json.dumps({"result": result})
            client_socket.send(response.encode())

        except Exception as e:
            client_socket.send(json.dumps({"error": str(e)}).encode())

        client_socket.close()

if __name__ == "__main__":
    start_server()
