'''
Q2

In automation, you often compare expected and actual outputs.
Write code to check if a test case passed or failed.

expected_title = "Dashboard"
actual_title = "Dashboard "

✅ Test Passed – Title matches


True - why >  Strip and convert them into the lowercase = both of them are equal.
'''

# Automation test case comparison with user input
# Ignores spaces and letter case

expected_title = input("Enter Expected Title: ")
actual_title = input("Enter Actual Title: ")

# Normalize inputs: remove extra spaces and ignore case
if expected_title.strip().lower() == actual_title.strip().lower():
    print("✅ Test Case Passed")
else:
    print("❌ Test Case Failed")
    print(f"Expected: '{expected_title}'")
    print(f"Actual_Result:   '{actual_title}'")