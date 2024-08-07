"""
We'll try to understand classes in python. 
Check the resources on google classroom to ensure you have gone through everything expected.

"""
###### THESE LISTS HAVE ALREADY BEEN DEFINED FOR YOU ###############
engineer_roster = [] # A list of all instantiated engineer objects
sales_roster = [] # List of all instantiated sales objects
branchmap = {  # A dictionary of dictionaries -> Maps branchcodes to cities and branch names
    0:  { "city": "NYC", "name": "Hudson Yards"},
    1:  { "city": "NYC" , "name": "Silicon Alley"},
    2:  { "city": "Mumbai", "name": "BKC"},
    3:  { "city": "Tokyo", "name": "Shibuya"},
    4:  { "city": "Mumbai", "name": "Goregaon"},
    5:  { "city": "Mumbai", "name": "Fort"}
}
####################################################################

class Employee:
    name : str 
    age : int
    ID : int
    city : int
    branches : list[int] # This is a list of branches (as branch codes) to which the employee may report
    salary : int 

    def __init__(self, name, age, ID, city,\
                 branchcodes, salary = None):
        self.name = name
        self.age = age 
        self.ID = ID
        self.city = city
        self.branches = branchcodes
        if salary is not None: self.salary = salary
        else: self.salary = 10_000 
    
    def change_city(self, new_city:str) -> bool:
        if self.city != new_city:
            self.city = new_city
            return True
        else:
            return False
        # Return true if city change, successful, return false if city same as old city

    def migrate_branch(self, new_code:int) -> bool:
        if len(self.branches) == 1:
            if branchmap[self.branches[0]]["city"] == branchmap[new_code]["city"]:
                self.branches[0] = new_code
            else:
                return False
        else:
            return False
        # Should work only on those employees who have a single 
        # branch to report to. Fail for others.
        # Change old branch to new if it is in the same city, else return false.

    def increment(self, increment_amt: int) -> None:
        self.salary += increment_amt
        return None
        # Increment salary by amount specified


class Engineer(Employee):
    position : str # Position in organization Hierarchy

    def __init__(self, name, age, ID, city,\
                 branchcodes, position= "Junior", salary = None):
        # Call the parent's constructor
        super().__init__(name, age, ID, city, branchcodes, salary)
        if position in ['Junior','Senior','Team Lead','Director']:
            self.position = position
        # Check if position is one of  "Junior", "Senior", "Team Lead", or "Director" 
        # Only then set the position. 

    
    def increment(self, amt:int) -> None:
        self.salary += 1.1*amt
        return None
        # While other functions are the same for and engineer,
        # and increment to an engineer's salary should add a 10% bonus on to "amt"
                
    def promote(self, position:str) -> bool:
        listOfPositionsAsc = ['Junior','Senior','Team Lead','Director']
        if listOfPositionsAsc.index(position) <= listOfPositionsAsc.index(self.position):
            return False
        else:
            self.position = position
            self.increment(0.3*self.salary)
            return True
        # Return false for a demotion or an invalid promotion
        # Promotion can only be to a higher position and
        # it should call the increment function with 30% of the present salary
        # as "amt". Thereafter return True.

class Salesman(Employee):
    """ 
    This class is to be entirely designed by you.

    Add increment (this time only a 5% bonus) and a promotion function
    This time the positions are: Rep -> Manager -> Head.

    Add an argument in init which tracks who is the superior
    that the employee reports to. This argument should be the ID of the superior
    It should be None for a "Head" and so, the argument should be optional in init.
    """
    
    # An extra member variable!
    superior : int # EMPLOYEE ID of the superior this guy reports to

    def __init__(self,name,age,ID,city,\
                 branchcodes,position = 'Rep', salary = None, sup = None): # Complete all this! Add arguments
        super().__init__(name,age,ID,city,branchcodes,salary)
        if position in ['Rep','Manager','Head']:
            self.position = position
        if position != 'Head':
            self.superior = sup
        else:
            self.superior = None
        
    def promote(self,pos) -> bool:
        posListAsc = ['Rep','Manager','Head']
        if posListAsc.index(self.position) >= pos:
            return False
        else:
            self.position = pos
            self.increment()
            return True

    def increment(self,amt) -> None:
        self.salary += 1.05*amt
        return None

    def find_superior(self) -> tuple[int, str]:
        if self.superior != None:
            for i in sales_roster:
                if i.ID == self.superior:
                    return (i.ID,i.name)
        else:
            return (None,None)
        # Return the employee ID and name of the superior
        # Report a tuple of None, None if no superior.

    def add_superior(self) -> bool:
        if self.position == 'Head':
            return False
        else:
            posListAsc = ['Rep','Manager','Head']
            check = True
            for i in sales_roster:
                if posListAsc.index(i.position) - posListAsc.index(self.position) == 1:
                    self.superior = i.ID
                    check = False
            if check:
                return False
            else:
                return True
        # Add superior of immediately higher rank.
        # If superior doesn't exist return false,


    def migrate_branch(self, new_code: int) -> bool:
        check + True
        for i in self.branches:
            if i == new_code:
                check = False
        if check:
            self.branches.append(new_code)
            return True
        else:
            return False
        # This should simply add a branch to the list; even different cities are fine

    





    
    
