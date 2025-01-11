import mysql.connector
from mysql.connector import Error
from http.server import BaseHTTPRequestHandler, HTTPServer
import json

# Database connection
def create_connection():
    try:
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='root',
            database='EmployeePayroll'
        )
        if connection.is_connected():
            return connection
    except Error as e:
        print(f"Error while connecting to MySQL: {e}")
        return None

# Fetch all employees
def get_employees():
    connection = create_connection()
    cursor = connection.cursor(dictionary=True)
    cursor.execute("SELECT * FROM Employees")
    employees = cursor.fetchall()
    cursor.close()
    connection.close()
    return employees

# Fetch all payroll logs
def get_payroll_log():
    connection = create_connection()
    cursor = connection.cursor(dictionary=True)
    cursor.execute("SELECT * FROM Payroll_Log")
    payroll_log = cursor.fetchall()
    cursor.close()
    connection.close()
    return payroll_log

# Fetch payroll data for an employee
def get_employee_payroll(employee_id):
    connection = create_connection()
    cursor = connection.cursor(dictionary=True)
    cursor.execute("SELECT * FROM Payroll_Log WHERE Employee_ID = %s", (employee_id,))
    payroll = cursor.fetchall()
    cursor.close()
    connection.close()
    return payroll

# Request handler for the HTTP server
class RequestHandler(BaseHTTPRequestHandler):

    # Handle GET requests
    def do_GET(self):
        if self.path == '/employees':
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            employees = get_employees()
            self.wfile.write(json.dumps(employees, default=str).encode())

        elif self.path == '/payroll':
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            payroll_log = get_payroll_log()
            self.wfile.write(json.dumps(payroll_log, default=str).encode())

        # Handle GET request for specific employee payroll
        elif self.path.startswith('/payroll/'):
            employee_id = self.path.split('/')[-1]
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            payroll_data = get_employee_payroll(employee_id)
            self.wfile.write(json.dumps(payroll_data, default=str).encode())

        else:
            self.send_response(404)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(b"Page not found")

# Run the server
def run(server_class=HTTPServer, handler_class=RequestHandler, port=9090):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f'Starting server on port {port}...')
    httpd.serve_forever()

if __name__ == "__main__":
    run()
