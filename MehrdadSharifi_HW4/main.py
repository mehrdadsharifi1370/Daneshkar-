from user import User
from getpass import getpass


class UserManager:
    def __init__(self, db_path):
        self.db_path = db_path

    def display_menu(self):
        print("- Enter 0 for exit")
        print("- Enter 1 for registration")
        print("- Enter 2 for login")

    def register_user(self):
        new_username = input("Enter username for registration: ")
        new_phonenumber = input(
            "Enter your phone number for registration (optional): ")
        new_password_register = getpass("Enter your password: ")

        try:
            if new_phonenumber:
                register = User(new_username, new_password_register,
                                new_phonenumber, path=self.db_path)
            else:
                register = User(
                    new_username, new_password_register, path=self.db_path)

            register.creat_new_user()
            print("Registration successful!")
        except Exception as e:
            print(f"An error occurred during registration: {e}")

    def login_user(self):
        username = input("Enter your username: ")
        password = getpass("Enter your password: ")
        inst = User(username=username, password=password, path=self.db_path)

        if inst.authenticate():
            self.manage_profile(inst)
        else:
            print("Your username or password is incorrect")

    def manage_profile(self, inst):
        while True:
            print("- Enter 1 for showing your profile details")
            print("- Enter 2 for editing your profile")
            print("- Enter 3 for changing your password")
            print("- Enter 4 for back to home page")
            selected_option = input("Console> ")

            if selected_option == "1":
                print(inst)
            elif selected_option == "2":
                change_username = input(
                    "Enter new username (leave blank to keep current): ")
                change_phone_number = input(
                    "Enter new phone number (leave blank to keep current): ")
                inst.edit_user_profile(
                    New_username=change_username or inst.username,
                    new_phone_number=change_phone_number or inst.phone_number,
                )
                print("Profile updated successfully!")
            elif selected_option == "3":
                self.change_password(inst)
            elif selected_option == "4":
                break
            else:
                print(
                    f"'{selected_option}' is not recognized as an internal command")

    def change_password(self, inst):
        crpassw = getpass("Enter current password: ")
        np = getpass("Enter new password: ")
        rnp = getpass("Repeat new password: ")

        if np == rnp:
            try:
                User.change_password(
                    path=self.db_path,
                    username=inst.username,
                    current_password=crpassw,
                    new_password=np,
                    repeated_password=rnp
                )
                print("Password changed successfully!")
            except Exception as e:
                print(f"An error occurred while changing the password: {e}")
        else:
            print("New passwords do not match.")


def main():
    user_manager = UserManager("Users.db")
    while True:
        user_manager.display_menu()
        command = input("Console> ")

        if command == "0":
            print("Exiting the program.")
            break
        elif command == "1":
            user_manager.register_user()
        elif command == "2":
            user_manager.login_user()
        else:
            print(f"'{command}' is not recognized as an internal command")


if __name__ == "__main__":
    main()
