username = "admin"
password = "1234"

a = input("Enter username: ")
b = input("Enter password: ")
if a == username and b == password:
    print("Login successful!")
else:
    print("Login failed. Please try again.")