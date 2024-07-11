"""
This is where the actual working of the program will happen!
We'll be Querying stuff for testing whether your classes were defined correctly

Whenever something inappropriate happens (like a function returning false in people.py),
raise a Value Error.
"""
from people import * # import everything!

if __name__ == "__main__":  # Equivalent to int main() {} in C++.
    last_input = 99
    while last_input != 0:
        last_input = int(input("Please enter a query number:"))

        if last_input == 1:
            name = input("Name: ")
            age = int(input('Age: '))
            ID = int(input("ID: "))
            city = input("City: ")
            branchcodes = list(int(i) for i in input("Branch(es):").split(','))
            # How will you conver this to a list, given that
            # the user will always enter a comma separated list of branch codes?
            # eg>   2,5

            salary = int(input("Salary: "))
            # Create a new Engineer with given details.
            engineer_instance = Engineer(name,age,ID,city,branchcodes,salary = salary) # Change this
            engineer_roster.append(engineer_instance) # Add him to the list! See people.py for definiton
        
        elif last_input == 2:
            name = input("Name: ")
            age = int(input('Age: '))
            ID = int(input("ID: "))
            city = input("City: ")
            branchcodes = list(int(i) for i in input("Branch(es):").split(','))
            position = input('Position: ')
            salary = int(input("Salary: "))
            salesman_instance = Salesman(name,age,ID,city,branchcodes,position,salary)
            sales_roster.append(salesman_instance)
            # Gather input to create a Salesperson
            # Then add them to the roster


        elif last_input == 3:
            ID = int(input("ID: "))
            # Print employee details for the given employee ID that is given. 
            found_employee = None
            for employee in engineer_roster + sales_roster:
                if employee.ID == ID:
                    found_employee = employee
                    break
            if not found_employee: print("No such employee")
            else:
                print(f"Name: {found_employee.name} and Age: {found_employee.age}")
                print(f"City of Work: {found_employee.city}")

                ## Write code here to list the branch names to
                ## which the employee reports as a comma separated list
                ## eg> Branches: Goregaon,Fort
                branch_names = []
                for i in found_employee.branches:
                    branch_names.append(branchmap[i]["name"])
                ## ???? what comes here??
                print(f"Branches: {branch_names}")
                print(f"Salary: {found_employee.salary}")

        elif last_input == 4:
            
            #### NO IF ELSE ZONE ######################################################
            # Change branch to new branch or add a new branch depending on class
            # Inheritance should automatically do this. 
            # There should be no IF-ELSE or ternary operators in this zone
            ID = int(input("ID: "))
            found_employee = None
            #### NO IF ELSE ZONE ENDS #################################################

        elif last_input == 5:
            ID = int(input("Enter Employee ID to promote: "))
            found_employee = None
            for employee in engineer_roster + sales_roster:
                if employee.ID == int(ID):
                    found_employee = employee
                    break
            if not found_employee: print("No such employee")
            else:
                posToProm = found_employee.position 
                found_employee.promote()
            # promote employee to next position

        elif last_input == 6:
            ID = int(input("Enter Employee ID to give increment: "))
            found_employee = None
            inc_amt = int(input("Enter increment: "))
            for employee in engineer_roster + sales_roster:
                if employee.ID == ID:
                    found_employee = employee
                    break
            if not found_employee: print("No such employee")
            else:
                found_employee.increment(inc_amt)
            # Increment salary of employee.
        
        elif last_input == 7:
            ID = int(input("Enter Employee ID to find superior: "))
            for i in sales_roster:
                if i.ID == ID:
                    print(i.find_superior())
            # Print superior of the sales employee.
        
        elif last_input == 8:
            ID_E = int(input("Enter Employee ID to add superior: "))
            ID_S = int(input("Enter Employee ID of superior: "))
            for i in sales_roster:
                if i.ID == ID_E:
                    i.superior = ID_S
            # Add superior of a sales employee
        elif last_input == 9:
            print("Thank you, you have exited editing.")
            print("***")
            break
        else:
            raise ValueError("No such query number defined!")


            
            

            


            


        






