# Student Grade Calculator

print("===== Student Grade Calculator =====")

subjects = int(input("Enter number of subjects: "))

marks = []

for i in range(subjects):
    while True:
        mark = float(input(f"Enter marks for Subject {i + 1} (0-100): "))

        if 0 <= mark <= 100:
            marks.append(mark)
            break
        else:
            print("Invalid marks! Please enter a value between 0 and 100.")

# Calculate total and percentage
total = sum(marks)
percentage = total / subjects

# Assign grade
if percentage >= 90:
    grade = "A"
elif percentage >= 80:
    grade = "B"
elif percentage >= 70:
    grade = "C"
elif percentage >= 60:
    grade = "D"
else:
    grade = "F"

# Display result
print("\n===== Student Result =====")
print("Total Marks:", total)
print("Percentage:", percentage, "%")
print("Grade:", grade)