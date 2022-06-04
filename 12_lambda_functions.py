add_numbers = lambda a, b: a+b
multiply_numbers = lambda a, b: a*b
divide_numbers = lambda a, b: a/b

name_list = ["Vári Róbert", "Kiss Elemér", "Nagy Adrienn", "Tóth Barna", "Kiss Elemér Aladár"]

# print(sorted(name_list))
# print(sorted(name_list, key=lambda name: name.split()[-1]))


student_list = {
    1: {"name": "Robert", "rating": 2},
    2: {"name": "Kriszta", "rating": 5},
    3: {"name": "Csaba", "rating": 4},
    4: {"name": "Tamás", "rating": 3},
}

def get_student_rating(student_id):
    rating = student_list[student_id]["rating"]
    return rating


# result = sorted(student_list, reverse=True, key=get_student_rating)
result = sorted(student_list, reverse=True, key=lambda student_id: student_list[student_id]["rating"])
for i in result:
    print(f"name: {student_list[i]['name']}, rating: {student_list[i]['rating']}")