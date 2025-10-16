user_age = int(input("Enter your age: \n"))
if user_age >= 18:
    print("Yes you can go to Goa and vote")
else:
    print("No, you can't go to Goa and vote")

# This can be converted into single line.
print("Yes you can go to Goa and vote") if user_age >= 18 else print("No, you can't go to Goa and vote")