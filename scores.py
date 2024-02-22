student_name = input("what is your name:")
course_work_score = int(input("what is your course work marks:"))
exam_score = int(input("what is your exam score:"))
exam_marks = exam_score / 100 * 70

print(f"Your exam mark is {exam_marks} ")
course_work_marks = course_work_score / 100 * 30 

print(f"Your course work mark is {course_work_marks}")

final_mark = course_work_marks + exam_marks
print(f"Your final mark is {final_mark}")