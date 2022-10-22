User_list = []

class User:
    def __init__(self, first_name, last_name, email, created_on):
        self.first_name = first_name.upper()
        self.last_name = last_name.upper()
        self.email = email.upper()
        self.created_on = created_on.upper()


    def change_first_name(self, new_name):
        self.first_name = new_name
    
    def change_last_name(self, new_name):
        self.last_name = new_name

    def group(self. group):
        pass

    def user_check(self):
        user_change = print(input("You don't like your first name? Insert name change."))
        User_list.append(user_change)


class Employee(User):
    def __init__(self,home_address,security_level,department,first_name, last_name,email,created_on):
        super().__init__(first_name, last_name,email,created_on)
        self.home_address = home_address.upper()
        self.department = department.upper()
        self.security_level = security_level.upper()
        self.identity = first_name.upper() + " " + last_name.upper() + " " + department.upper()
     
    

    def change_first_name(self, new_name):
        self.first_name = new_name
    
    def change_last_name(self, new_name):
        self.last_name = new_name

    def change_department(self):
        new_department = print(input("Insert new name: "))
        self.department = new_department
        return self.department

   
    def __str__(self):
        return f" | {self.first_name}{self.last_name} in {self.department}"
    
    
    def __repr__(self):
        return f"Employee | {self.first_name} {self.last_name} {self.home_address} {self.security_level} {self.email} {self.created_on}>"
worker = Employee('15 Main Street','Clearance-4','Security','Hugh','Jaenus','hughjaenus@brownmail.com','July 3, 2004')
User_list.append(worker)
worker = Employee('15 Main Street','Clearance-4','Security','Ivana','Tinkle','peepee@brownmail.com','April 9, 2008')
User_list.append(worker)
worker = Employee('15 Main Street','Clearance-4','Security','Anita','Bath','tublover23@brownmail.com','July 3, 2006')
User_list.append(worker)

# print(worker.identity)
# print(isinstance("hello", str))
# print(isinstance("hello", int))
# print(isinstance(worker, Employee))
# print(isinstance(worker, User))

class Customer(User):
    def __init__(self,billing_address,shipping_address,first_name, last_name,email,created_on, purchase_history):
            super().__init__(first_name, last_name,email,created_on)
            self.billing_address = billing_address.upper()
            self.shipping_address =shipping_address.upper()
            self.purchase_history = purchase_history.upper()
            self.identity = email.upper() + " " + shipping_address.upper()



    def change_first_name(self, new_name):
        self.first_name = new_name
    
    def change_last_name(self, new_name):
        self.last_name = new_name
    def change_billing_address(self):
        new_billing = print(input("Insert new billing address: "))
        self.billing_address = new_billing
        return self.billing_address
    def change_shipping_address(self):
        new_shipping = print(input("Insert new shipping address: "))
        self.shipping_address = new_shipping
        return self.shipping_address



    def __str__(self):
        return f"<Customer |{self.email}{self.shipping_address}>"
    
 
    def __repr__(self):
        return f"<Customer |{self.first_name} {self.last_name} {self.billing_address} {self.shipping_address} {self.email} {self.created_on}"

normo = Customer('1615 W Spooner St','1615 W Spooner St', 'Sally','Vaugh','saliva@email.com','April 1, 2016','[sandbag, rope, disinfectant wipes]')
User_list.append(normo)
normo = Customer('10 N Main St','1516 N Winkle St', 'Dingle','Vaughn','salivah@email.com','July 3, 2016','[Duct tape, ski mask, disposible gloves]')
User_list.append(normo)
normo = Customer('2419 S 24th St','2419 S 24th St', 'Ollie','Tabooger','snotlord69@email.com','July 3, 2016','[Duct tape, ski mask, disposible gloves]')
User_list.append(normo)
# print(normo.identity)
# print(isinstance("hello", str))
# print(isinstance("hello", int))
# print(isinstance(normo, Customer))
# print(isinstance(normo, User))

print(User_list.sort())



#TO-DO:
# Any Two Users are the same if they have the same email
# All Users should be hashable
# If I have a list of Users and sort them they should be sorted by there created_on date

