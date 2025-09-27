import socket
import json

grading_scheme = [
    (4.33, "A+", "Excellent"),
    (4.00, "A", "Excellent"),
    (3.66, "A-", "Very good"),
    (3.33, "B+", "Very good"),
    (3.00, "B", "Very good"),
    (2.66, "B-", "Good"),
    (2.33, "C+", "Good"),
    (2.00, "C", "Good"),
    (1.66, "C-", "Passable"),
    (1.33, "D+", "Passable"),
    (1.00, "D", "Passable"),
    (0.00, "E", "Failure")
]

def get_grade_info(grade_point):
    for gp, grade, qualification in grading_scheme:
        if grade_point >= gp:
            return grade, qualification
    return "E", "Failure"

def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(("127.0.0.1", 6000))
    server_socket.listen(5)
    print("Server started. Waiting for clients...")

    while True:
        client_socket, address = server_socket.accept()
        print(f"Connection from {address}")

        try:
            data = client_socket.recv(1024).decode()
            grade_point = float(data)

            letter_grade, qualification = get_grade_info(grade_point)

            response = {
                "letter_grade": letter_grade,
                "qualification": qualification
            }
            client_socket.send(json.dumps(response).encode())

        except Exception as e:
            client_socket.send(json.dumps({"error": str(e)}).encode())

        client_socket.close()

if __name__ == "__main__":
    start_server()
