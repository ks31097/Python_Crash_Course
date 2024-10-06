class Privileges():
    def __init__(self, *admin_privileges):
        self.privileges = admin_privileges

    def show_privileges(self):
        print("Admin privileges: ")
        for privilege in self.privileges:
            print(f"\t {privilege}")