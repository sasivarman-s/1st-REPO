admin="admin1"
password="1234567890"

a=str(input("Enter your username: "))
p=str(input("Enter your password: "))
if a==admin and p==password:
    print("Login successful!")  
 else:
    print("Login failed. Please check your username and password.")   
