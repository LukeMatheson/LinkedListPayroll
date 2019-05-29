# Luke Matheson, ID: lcm95
from Employee import *
from LinkedList import *

employeeList = LinkedList()

loop = True
while loop:
    print('*** CS 172 Payroll Simulator ***')
    print('A. Add New Employee')
    print('B. Enter Hours Worked')
    print('C. Display Payroll')
    print('D. Update Employee Pay Rate')
    print('E. Remove Employee from Payroll')
    print('F. Exit the program')
    userInput = input('Enter your choice: ')
    if userInput.lower() == 'a':
        loop2 = True
        id_input = ""
        while loop2:
            id_input = input('Enter the new employee ID: ')
            if employeeList.search(id_input):
                print('That employee already exists, please try a new ID')
            else:
                loop2 = False
        hourly_rate = input('Enter the hourly rate: ')
        newEmployee = Employee(id_input, hourly_rate)
        employee_node = Node(newEmployee)
        employeeList.append(employee_node)
        employeeList[(len(employeeList) - 2)].setNext(employeeList[(len(employeeList) - 1)])

    elif userInput.lower() == 'b':
        for x in range(len(employeeList)):
            new_hours = input('Enter hours worked for Employee ' + employeeList[x].getData().getID() + ': ')
            loop3 = True
            while loop3:
                if new_hours[0] == '-':
                    print("No negative hours worked, please try again.")
                    new_hours = input('Enter hours worked for Employee ' + employeeList[x].getData().getID() + ': ')
                else:
                    loop3 = False
            employeeList[x].getData().setHours(new_hours)
            employeeList[x].getData().setWages()

    elif userInput.lower() == 'c':
        print('*** Payroll ***')
        if len(employeeList) == 0:
            print('None')
        else:
            for x in range(len(employeeList)):
                print(employeeList[x].getData())

    elif userInput.lower() == 'd':
        id_input = input('Enter the employee ID: ')
        loop4 = True
        while loop4:
            if employeeList.search(id_input) == False:
                print('That is not a valid employee ID')
                new_rate = input('Enter the employee ID: ')
            else:
                loop4 = False
        check = 0
        for x in range(len(employeeList)):
            if employeeList[x].getData().getID() == id_input.lower():
                new_rate = input('Enter new hourly rate for Employee ' + employeeList[x].getData().getID() + ': ')
                loop5 = True
                while loop5:
                    if float(new_rate) < 6.00:
                        print('Hourly rate must be greater than 6.00')
                        new_rate = input('Enter new hourly rate for Employee ' + employeeList[x].getData() + ': ')
                    else:
                        loop5 = False
                employeeList[x].getData().setRate(new_rate)
                employeeList[x].getData().setWages()
                break

    elif userInput.lower() == 'e':
        remove_ID = input('Enter the ID of the employee to remove from payroll: ')
        check = 0
        for x in range(len(employeeList)):
            if employeeList[x].getData().getID().lower() == remove_ID.lower():
                check += 1
                employeeList.remove(employeeList[x])
                break
        if check == 0:
            print('That is an invalid employee ID')
    elif userInput.lower() == 'f':
        loop = False
        print('Good-Bye!')

    else:
        print('Invalid input. Please try again')
