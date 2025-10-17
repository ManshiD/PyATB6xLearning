'''Check if the user can log in based on correct username and password.

I/p

username = "admin"
password = "1234"

O/p
✅ Login Successful


For the Fail condition Other O/P = ❌ Invalid Credentials'''

# Simple login validation
correct_username = "admin"
correct_password = "12345"

# user = input("Enter username: ")
# pwd = input("Enter password: ")
#
# if user == correct_username and pwd == correct_password:
#     print("✅ Login Successful")
# else:
#     print("❌ Invalid Credentials")

correct_username = "admin"
correct_password = "12345"

for attempt in range(3):
    user = input("Enter username: ")
    pwd = input("Enter password: ")

    if user == correct_username and pwd == correct_password:
        print("✅ Login Successful!")
        break
    else:
        print(f"❌ Wrong credentials! Attempts left: {2 - attempt}")
else:
    print("🔒 Account locked due to too many failed attempts _so many times.")