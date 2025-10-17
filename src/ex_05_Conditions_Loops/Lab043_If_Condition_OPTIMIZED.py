# Write a program to take a user age and
# let him know if he can go to club
# 21

# Logic Building Formula
# Step 1
# i/p - age int
# o/p - String (result - Can go to club or not)

# Step 2 Rough logic (brute force)
# age > 21 -> print can go
# age < 21 -> print can't go

# Step 3 write the logic
age=int(input("Enter the age\n").strip())

if age <= 0 or age > 130:
    print("Enter a valid age")
else:
    print("Enter a valid age")
if age> 21:
    print("Yes, you can go to club.")
else:
    print("No, you can't go to club.")

# Step 4: Check for edge cases.
# We should consider edge cases such as:
# Negative ages are extremely high values -> program will break.
# Non-numeric input - ABC
# Age which is valid > 130

# Step5: Handle all edge cases





