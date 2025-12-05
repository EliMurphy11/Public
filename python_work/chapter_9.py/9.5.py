# dd an atrribute called login_attempts to your User class from 9.3.py. write a method called increment_login_attempts() that increments the value of login_attempts by 1.
# write another method called reset_login_attempts() that resets the value of login_attempts to 0.
from users import user
class user:
    """Trying to represent a user"""
    def __init__(self, first_name, last_name, age, city):
        """initialize the attributes of the user"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.login_attempts = 0

    def greet_user(self):
        """greet the user"""
        print(f"Hello, {self.first_name} {self.last_name} from {self.city}!.")
        
    def describe_user(self):
        """display a summary of the user's information"""
        print(f"User Information:\nName: {self.first_name} {self.last_name}\nAge: {self.age}\nCity: ")

    def increment_login_attempts(self):
        """increment the value of login_attempts by 1"""
        self.login_attempts += 1

    def reset_login_attempts(self):
        """reset the value of login_attempts to 0"""
        self.login_attempts = 0