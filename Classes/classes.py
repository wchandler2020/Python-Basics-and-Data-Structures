#polymorpheus

#inheritence
class User:
    def log(self):
        print(self)

class Instructor(User):
    def log(self):
        print("i am the teacher")
#encapsulation

class Customer(User):
    #very similar to a constructor in C#, Javascript or Java ect...
    def __init__(self, name, membership_type):
        self.name = name
        self.membership_type = membership_type

    ##getter
    @property
    def name(self):
        print("getting name")
        return self._name

    #setter
    @name.setter
    def name(self, name):
        print("setting name")
        self._name = name

    def print_customer(self):
        print("getting customer from DB....")
    #overrides the string method so that you seen not just the memory location but an string representation
    def __str__(self):
        return "Hi " + self.name + " Your Membership is " + self.membership_type

    # def get_all_customer(customers):
    #     for customer in customers:
    #         print(customer)

    #overriding the comparision and allows to compare the arguments and not just the memory location.
    def __eq__(self, other):
        if self.name == other.name and self.membership_type == other.membership_type:
            return  True
        else:
            return False

customers = [Customer("William", "Gold"), Customer("Kerry", "Silver"), Instructor()]

for user in customers:
    print(user.log())

# print(customers[0].log(), customers[1].log())











