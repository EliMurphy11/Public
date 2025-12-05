class user:
    """Trying to represent a user"""
    def __init__(self, first_name, last_name, age, city):
        """initialize the attributes of the user"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.city = city
def describe_user(self):
        """display a summary of the user's information"""
        print(f"User Information:\nName: {self.first_name} {self.last_name}\nAge: {self.age}\nCity: {self.city}")
def greet_user(self):
        """greet the user"""
        print(f"Hello, {self.first_name} {self.last_name}! from {self.city}.")
def greet_user(self):
        """greet the user"""
        print(f"Hello, {self.first_name} {self.last_name} from {self.city}!.")
def describe_user(self):
        """display a summary of the user's information"""
        print(f"User Information:\nName: {self.first_name} {self.last_name}\nAge: {self.age}\nCity: {self.city}")
user1 = user("eli", "murphy", "16","mckinney",)
user2 = user("sarah", "jones", "25","mckinney")
user3 = user("mike", "johnson", "30","mckinney")
user4 = user("linda", "williams", "45","mckinneyville")
describe_user(user1)
greet_user(user1)
describe_user(user2)
greet_user(user2)
describe_user(user3)
greet_user(user3)
describe_user(user4)
greet_user(user4)
