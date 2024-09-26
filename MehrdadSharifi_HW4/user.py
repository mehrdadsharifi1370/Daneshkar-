from hashlib import sha256
from sqlite3 import connect
from uuid import uuid5, NAMESPACE_X500


class User:

    def __init__(self, username: str, password: str, path: str, phone_number: str = "None") -> None:
        self.username = username
        self.phone_number = phone_number
        self.password = password
        self.id = uuid5(NAMESPACE_X500, self.username)
        self.path = path

    def final_check(self) -> bool:
        """Check Username is exist and check password lenght"""
        if (User.__Is_Username_exist(self, self.username)):
            return "Exist"
        elif len(str(self.password)) < 4:
            return "NotSecure"
        else:
            return "ok"

    def __Is_Username_exist(self, usr: str) -> bool:
        """This function can find same usernames in DB"""
        # Connect to the SQLite database
        connection = connect(self.path)  # Replace with your database file
        cursor = connection.cursor()
        # Check if a username exists
        username_to_check = usr  # Replace with the username you want to check
        cursor.execute(
            "SELECT COUNT(*) FROM Usernames WHERE username = ?", (username_to_check))
        result = cursor.fetchone()
        username_exists = result[0] > 0
        # Close the cursor and connection
        if username_exists:
            cursor.close()
            connection.close()
            return True
        else:
            cursor.close()
            connection.close()
            return False

    def creat_new_user(self) -> bool:
        """Creating New User"""
        # Connect to the SQLite database
        connection = connect(self.path)  # Replace with your database file
        cursor = connection.cursor()
        # Insert the new values into the Users table
        chk = User.final_check(self)
        if chk == "Exist":
            cursor.close()
            connection.close()
            print("This username already exist")

        elif chk == "NotSecure":
            cursor.close()
            connection.close()
            print("Password is not secure")
        else:
            cursor.execute('''
                    INSERT INTO Usernames (Username,Password,ID,PhoneNumber)
                    VALUES (?, ?, ?, ?)
                    ''', (self.username, sha256(str(self.password).encode("utf-8")).hexdigest(), str(self.id), self.phone_number))
            # Commit the changes
            connection.commit()
            # Close the cursor and connection
            cursor.close()
            connection.close()

    def __str__(self):
        if self.id is not None:
            return f"Username: {self.username}\nUser ID: {self.id}\nPhone Number: {self.phone_number}"
        else:
            return "User not found!"

    def authenticate(self) -> bool:
        # Connect to the SQLite database (or your specific database)
        conn = connect(self.path)
        cursor = conn.cursor()

        # Prepare the SQL query to prevent SQL injection
        query = "SELECT * FROM usernames WHERE username = ? AND password = ?"

        # Execute the query with the provided username and password
        cursor.execute(query, (self.username, str(
            sha256(self.password.encode("utf-8")).hexdigest())))

        # Fetch the result
        user = cursor.fetchone()

        # Close the connection
        conn.close()

        # Check if user exists
        if user:
            print("Sucessfully Login")
            return True
        else:
            print("Login failed")
            return False

    def edit_user_profile(self, New_username: str, new_phone_number: str = "None") -> None:
        # Connect to the SQLite database
        conn = connect(self.path)  # Replace with your database file
        cursor = conn.cursor()

        # Prepare the SQL query to update the phone number
        query = "UPDATE Usernames SET PhoneNumber = ? WHERE Username = ?"

        # Execute the update query
        cursor.execute(query, (new_phone_number, self.username))
        query = "UPDATE Usernames SET Username = ? WHERE Username = ?"
        cursor.execute(
            "SELECT COUNT(*) FROM Usernames WHERE username = ?", (New_username))
        result = cursor.fetchone()
        username_exists = result[0] > 0
        # Close the cursor and connection
        if username_exists:
            print("This username already exist")
            cursor.close()
            conn.close()
        else:
            cursor.execute(query, (New_username, self.username))
            print("Sucessfully changed")
            cursor.close()
            conn.close()

    @staticmethod
    def change_password(path: str, username: str, current_password: str, new_password: str, repeated_password: str) -> bool:
        """Change the user's password."""
        if new_password != repeated_password:
            print("New passwords do not match.")
            return False

        conn = connect(path)
        cursor = conn.cursor()
        cursor.execute(
            "SELECT Password FROM Usernames WHERE Username = ?", (username,))
        result = cursor.fetchone()
        cursor.close()
        conn.close()

        if result and str(sha256(current_password.encode("utf-8")).hexdigest()) == result[0]:
            conn = connect(path)
            cursor = conn.cursor()
            cursor.execute("UPDATE Usernames SET Password = ? WHERE Username = ?", (sha256(
                new_password.encode("utf-8")).hexdigest(), username))
            conn.commit()
            cursor.close()
            conn.close()
            return True
        else:
            print(result[0])
            print("Current password is incorrect.")
            return False
