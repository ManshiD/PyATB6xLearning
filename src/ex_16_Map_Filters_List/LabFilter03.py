names = ["QA", "", "Automation", "", "Tester", ""]

def non_empty(x):
    if x!= "":
        return True
    else:
        return False

non_emptylist = list(filter(non_empty, names))
print(non_emptylist)