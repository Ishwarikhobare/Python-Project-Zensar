-- Create Database
CREATE DATABASE IF NOT EXISTS EmployeePayroll;

-- Use the created database
USE EmployeePayroll;

-- Create Employees Table
CREATE TABLE Employees (
    Employee_ID INT PRIMARY KEY AUTO_INCREMENT,
    Employee_Name VARCHAR(100) NOT NULL,
    Department VARCHAR(50) NOT NULL,
    Base_Salary DECIMAL(15, 2) NOT NULL,
    Bonus DECIMAL(15, 2) DEFAULT 0,
    Deductions DECIMAL(15, 2) DEFAULT 0,
    Net_Salary DECIMAL(15, 2),
    Created_Date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Create Attendance Table
CREATE TABLE Attendance (
    Attendance_ID INT PRIMARY KEY AUTO_INCREMENT,
    Employee_ID INT NOT NULL,
    Days_Worked INT NOT NULL,
    Total_Days INT DEFAULT 30,
    FOREIGN KEY (Employee_ID) REFERENCES Employees(Employee_ID)
);

-- Create Salary Slabs Table
CREATE TABLE Salary_Slabs (
    Slab_ID INT PRIMARY KEY AUTO_INCREMENT,
    Min_Salary DECIMAL(15, 2) NOT NULL,
    Max_Salary DECIMAL(15, 2) NOT NULL,
    Tax_Percentage DECIMAL(5, 2) NOT NULL
);

-- Create Payroll Log Table
CREATE TABLE Payroll_Log (
    Payroll_ID INT PRIMARY KEY AUTO_INCREMENT,
    Employee_ID INT NOT NULL,
    Net_Salary DECIMAL(15, 2) NOT NULL,
    Payment_Date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (Employee_ID) REFERENCES Employees(Employee_ID)
);

-- Insert Sample Data into Employees Table
INSERT INTO Employees (Employee_Name, Department, Base_Salary, Bonus, Deductions) 
VALUES 
('Alice Johnson', 'IT', 50000, 5000, 2000),
('Bob Smith', 'HR', 40000, 3000, 1500);

-- Insert Sample Data into Attendance Table
INSERT INTO Attendance (Employee_ID, Days_Worked) 
VALUES 
(1, 28),
(2, 25);

-- Insert Sample Data into Salary Slabs Table
INSERT INTO Salary_Slabs (Min_Salary, Max_Salary, Tax_Percentage) 
VALUES 
(0, 30000, 5),
(30001, 60000, 10);

-- Insert Sample Data into Payroll Log Table
-- This will be updated later based on net salary calculation
