# Program to check exam eligibility of a user

def check_exam_eligibility(attendance_percentage, minimum_required=75):
    if attendance_percentage >= minimum_required:
        return "Eligible for the exam."
    else:
        return "Not eligible for the exam. Attendance is below the required percentage."

# Input from the user
try:
    total_classes = int(input("Enter the total number of classes held: "))
    attended_classes = int(input("Enter the number of classes attended: "))

    if total_classes <= 0:
        print("Total classes must be greater than zero.")
    elif attended_classes < 0 or attended_classes > total_classes:
        print("Attended classes must be between 0 and the total classes.")
    else:
        # Calculate attendance percentage
        attendance = (attended_classes / total_classes) * 100
        print(f"Your attendance percentage is: {attendance:.2f}%")

        # Check eligibility
        result = check_exam_eligibility(attendance)
        print(result)

except ValueError:
    print("Please enter valid numeric values.")