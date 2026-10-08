#ASSIGMENT_01
students = {
    101: {"name": "Rahul", "branch": "CSE", "marks": 85},
    102: {"name": "Priya", "branch": "ECE", "marks": 90}
}


students[103] = {"name": "Aman", "branch": "ME", "marks": 78}


del students[102]
students[101]["marks"] = 88


student_tuple = (101, "Rahul", "CSE", 88)
student_list = [103, "Aman", "ME", 78]

print("Final Student Records:")
for roll_no, details in students.items():
    print(roll_no, details)

