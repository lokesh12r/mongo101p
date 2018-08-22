from pymongo import MongoClient


def grades_list(grades):
    sort_keys = [('student_id', 1),('type',1), ('score', 1)]
    return grades.find().sort(sort_keys)



connection = MongoClient("mongodb://localhost")
db = connection.students
grades = db.grades

student_marks = grades_list(grades)
student_id = ''

for item in student_marks:
    if item['student_id'] != student_id and item['type'] == 'homework':
                grades.delete_one(item)
                student_id=item['student_id']
