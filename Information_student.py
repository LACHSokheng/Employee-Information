n = int(input("Enter the number of students: "))
students = []

for i in range(n):
    print(f'Student {i + 1} :')
    id = int(input('Enter your ID: '))
    name = input("Enter your name: ")
    ca = float(input("Enter Score of Computer Architecture:"))
    dc = float(input("Enter Score of Data Communication:"))
    db = float(input("Enter Score of Database:"))
    ds = float(input("Enter Score of Data Structure Algorithm:"))
    en = float(input("Enter Score of English:"))
    cp = float(input("Enter Score of C++ programming:"))

    total = ca + dc + ds + db + en + cp
    avg = total / 6

    # Determine the grade
    if avg >= 90:
        grade = 'A'
    elif avg >= 80:
        grade = 'B'
    elif avg >= 70:
        grade = 'C'
    elif avg >= 60:
        grade = 'D'
    elif avg >= 50:
        grade = 'E'
    else:
        grade = 'F (Fail)'
    print('Total: {:.2f}'.format(total))
    print("Average: {:.2f}".format(avg))
    print("Grade: ",grade)

    students.append({'ID': id, 'Name': name, 'CA': ca, 'DC': dc, 'DS': ds, 'DB': db, 'Eng': en, 'Cpp': cp, 'Total': total, 'Avg': avg, 'Grade': grade})
    print()

# Sort students based on average score in descending order
sorted_students = sorted(students, key=lambda x: x['Avg'], reverse=True)

print("\nResults:")
print("{:<10} {:<15} {:<5} {:<5} {:<5} {:<5} {:<5} {:<5} {:<10} {:<10} {:<10}".format(
    "ID", "Name", "CA", "DC", "DS", "DB", "Eng", "Cpp", "Total", "Avg", "Grade"))
print("------------------------------------------------------------------------------")

for student in sorted_students:
    print("{:<10} {:<15} {:<5} {:<5} {:<5} {:<5} {:<5} {:<5} {:<10} {:<10.2f} {:<10}".format(student['ID'], student['Name'], student['CA'],
                                                                                      student['DC'], student['DS'],
                                                                                      student['DB'], student['Eng'],
                                                                                      student['Cpp'], student['Total'], student['Avg'], student['Grade']))
