n = int(input('Input Number of Employee: '))

Employee = []

for i in range(n):
    salary = 250
    
    print(f'Employee {i+1}:')
    id = int(input('Input ID:'))
    name = input('Input Name:')
    sex = input('Input Sex:')
    hours = int(input('Input Hours: '))
    OTH = max(hours - 45, 0)
    print('OT(Hours) :' + str(OTH))# Calculate OT hours, limited to a minimum of 0
    OTR = float(input('Input OT(Rate): '))
    depre = 0  # Initialize depre variable
    SalaryMonth = 0  # Initialize SalaryMonth variable

    if hours < 35:
        depre = (salary * 25) / 100
        SalaryMonth = salary - depre

    elif hours >= 35 and hours <= 45:
        SalaryMonth = salary

    else:
        SalaryMonth = salary + OTH * OTR
    
    print('Salary deduction :' +str(depre))

    Employee.append({'ID': id, 'Name': name, 'Sex': sex, 'Salary': salary, 'Hours': hours, 'OTH': OTH, 'OTR': OTR, 'Depre': depre, 'SalaryMonth': SalaryMonth})


print("\nResults:")
print("{:<5} {:<15} {:<7} {:<10} {:<5} {:<10} {:<10} {:<10} {:<10}".format("ID", "Name", "Sex", "Salary", "Hours", "OT(hours)", "OT(Rate)", "Depre", "Salary in Month"))
print("---------------------------------------------------------------------------------")

for emp in Employee:
    print("{:<5} {:<10} {:<5} ${:<10.2f} {:<5} {:<10} {:<10} ${:<10.2f} ${:<10.2f}".format(emp['ID'], emp['Name'], emp['Sex'], emp['Salary'], emp['Hours'], emp['OTH'], emp['OTR'], emp['Depre'], emp['SalaryMonth']))
    