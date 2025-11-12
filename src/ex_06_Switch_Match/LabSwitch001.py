'''
Condition
1. If else
2. Switch
There is no traditional switch statement like in C, Java or Javascript -
but there are several ways to achieve the same functionality.

match-case (Python 3.10+ feature)
1. There is no concept of break here
2. match will match with whatever you have mentioned with the case.
default is _
'''

day = int(input("Enter the day\n"))
match day:
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case 3:
        print("Wednesday")
    case 4:
        print("Thursday")
    case 5:
        print("Friday")
    case 6:
        print("Saturday")
    case 7:
        print("Sunday")
    case _:
        print("Invalid input")