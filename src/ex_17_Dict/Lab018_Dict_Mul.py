student_infor1 = {
    "name":"Pramod",
    "sge":67,
    "address": {
        "home_address":  "ND",
        "office_address":  "KA",
    },
}

student_infor2 = {
    "name":"Pramod",
    "sge":67,
    "address": {
        "home_address":  "ND",
        "office_address":  "KA",
    },
}

student_infor3 = {
    "name":"Pramod",
    "sge":67,
    "address": {
        "home_address":  "PODI",
        "office_address":  "vizag",
    },
}
student_list = [student_infor1, student_infor2, student_infor3]
print(student_list)
print(student_list[0]["name"])
print(student_list[2]["address"]["office_address"])
