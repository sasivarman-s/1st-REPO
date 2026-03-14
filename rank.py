attendance = float(input("Enter Attendance Percentage: "))
study_hours = float(input("Enter Study Hours per Day: "))
internal_marks = float(input("Enter Internal Marks: "))

student_data = attendance, study_hours, internal_marks

score = (attendance * 0.3) + (study_hours * 10) + (internal_marks * 0.5)

if attendance >= 75 and internal_marks >= 40 and study_hours >= 2:
    result = "PASS"
else:
    result = "FAIL"

print("Student Data:", student_data)
print("Calculated Performance Score:", score)
print("Predicted Result:", result)
