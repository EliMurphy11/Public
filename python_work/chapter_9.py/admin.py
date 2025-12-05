# ...existing code...
from users import user

class Admin(user):
    """Admin user with a list of privileges."""
    def __init__(self, first_name, last_name, age, city):
        super().__init__(first_name, last_name, age, city)
        self.privileges = ["can add post", "can delete post"]


    def show_privileges(self):
        for privilege in self.privileges:
            print(privilege)
# ...existing code...
if __name__ == "__main__":
    admin = Admin("Regina", "Murphy", "12", "mckinney")
    admin.show_privileges()
    admin = ("regina murphy")
    privileges = ("can add post", "can delete post")


 
