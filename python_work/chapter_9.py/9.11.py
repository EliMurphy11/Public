import ice_cream_stand
class User:
    """A basic user."""
    def __init__(self, first_name, last_name, **kwargs):
        self.first_name = first_name
        self.last_name = last_name
        for k, v in kwargs.items():
            setattr(self, k, v)

    def describe_user(self):
        print(f"{self.first_name} {self.last_name}")


class Privileges:
    """Store and show a list of privileges."""
    def __init__(self, privileges=None):
        self.privileges = privileges or ["can add post", "can delete post"]

    def show_privileges(self):
        print("Privileges:")
        for p in self.privileges:
            print(f"- {p}")


class Admin(User):
    """User with administrative privileges."""
    def __init__(self, first_name, last_name, privileges=None, **kwargs):
        super().__init__(first_name, last_name, **kwargs)
        self.privileges = Privileges(privileges)

    def show_privileges(self):
        self.privileges.show_privileges()
    