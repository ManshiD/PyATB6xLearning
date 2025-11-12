print("Enter which type of Test you want to run")
test_type = input("Enter the Test type: API, UI, Performance, Security")

match test_type:
    case "API":
        print("We are running a POSTMAN API testcase.")
    case "UI":
        print("We are running a Selenium testcase.")
    case "Performance":
        print("We are running a Performance testcase.")
    case "Security":
        print("We are running a Security testcase.")
    case _:
        print("Invalid Type.")
