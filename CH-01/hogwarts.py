# students = ["Hermione", "Harry", "Ron", "Draco"]
# houses = ["Gryffindor", "Gryffindor", "Gryffindor", "Slytherin"]

# P1
# print(students)

# P2
# print(students[0])
# print(students[1])
# print(students[2])

# P3
# for student in students:
#     print(student)

# P4
# for i in range(len(students)):
#     print(i + 1, students[i])

# P5
# students = {"Hermione": "Gryffindor",
#             "Harry": "Gryffindor",
#             "Ron": "Gryffindor",
#             "Draco": "Slytherin",
#             }
#
# # print(students["Hermione"])
# # print(students["Harry"])
# # print(students["Ron"])
# # print(students["Draco"])
#
# for student in students:
#     print(student, students[student], sep=", ")


students = [
    {"name": "Hermione", "house": "Gryffindor", "patronus": "Otter"},
    {"name": "Harry", "house": "Gryffindor", "patronus": "Stag"},
    {"name": "Ron", "house": "Gryffindor", "patronus": "Jack Russel terrier"},
    {"name": "Draco", "house": "Slytherin", "patronus": None}
]

for student in students:
    print(student["name"], student["house"], sep=", ")



