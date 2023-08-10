n = int(input('Input Number of Employee: '))

Employee = []

for i in range(n):
    depre = 0  # Initialize depre variable
    OTR = 0
    print(f'Employee {i + 1}:')

    id = int(input('Input ID:'))
    name = input('Input Name:')
    sex = input('Input Sex:')
    salary = float(input('Input Salary :'))
    hours = int(input('Input Hours: '))
    OTH = max(hours - 45, 0)
    print('OT(Hours) :' + str(OTH)) # Calculate OT hours, limited to a minimum of 0
    # OTR = float(input('Input OT(Rate): '))
    SalaryMonth = 0  # Initialize SalaryMonth variable

    if hours < 35:
        percent = int(input('Input Percent : '))
        depre = (salary * percent) / 100
        print('Salary deduction :' + str(depre))
        SalaryMonth = salary - depre

    elif hours >= 35 and hours <= 45:
        OTR = float(input('Input OT(Rate): '))
        SalaryMonth = salary

    else:
        OTR = float(input('Input OT(Rate): '))
        SalaryMonth = salary + OTH * OTR


    Employee.append({
        'ID': id,
        'Name': name,
        'Sex': sex,
        'Salary': salary,
        'Hours': hours,
        'OTH': OTH,
        'OTR': OTR,
        'Depre': depre,
        'SalaryMonth': SalaryMonth
    })


print("\nResults:")
print("--------------------------------------------------------------------------------------------")
print("{:<5} {:<10} {:<10} {:<10} {:<10} {:<10} {:<10} {:<10} {:<10}".format("ID", "Name", "Sex", "Salary", "Hours", "OT(hours)", "OT(Rate)", "Depre", "Salary in Month"))
print("--------------------------------------------------------------------------------------------")

for emp in Employee:
    print("{:<5} {:<10} {:<10} ${:<10.2f} {:<10} {:<10} ${:<10} ${:<10.2f} ${:<10.2f}".format(
        emp['ID'], emp['Name'], emp['Sex'], emp['Salary'], emp['Hours'], emp['OTH'], emp['OTR'],
        emp['Depre'], emp['SalaryMonth']))
    