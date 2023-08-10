n = int(input("Enter number of Employees :"))
employees = []
while n > 0:
    OT_rate = 0
    percent = 0
    code = input("Enter code :")
    name = input("Enter Name employee :")
    gender = input("Enter Gender :")
    salary = int(input("Enter Salary :"))
    hours = int(input("Enter hour :"))
    if hours > 45:
        OT_rate = int(input("Enter OT(rate) :"))
        OT_hours = hours - 45
        Depr = "_____"
        total_salary = salary + (OT_hours * OT_rate)
        print(f'Salary in month: {total_salary}')
    elif 35 <= hours <= 45:
        OT_hours = '_____'
        Depr = "_____"
        total_salary = salary
        print(f'Salary in month: {total_salary}')
    else:
        percent = int(input("Enter percent :"))
        OT_hours = '_____'
        Depr = (salary * percent) / 100
        print(f'Depreciation: {Depr}')
        total_salary = salary - Depr
        print(f'Salary in month: {total_salary}')
    employee = {
        'code': code,
        'name': name,
        'gender': gender,
        'salary': salary,
        'hours': hours,
        'OT_hours': OT_hours,
        'OT_rate': OT_rate,
        'Depr': Depr,
        'total_salary': total_salary
    }
    employees.append(employee)
    n -= 1
print("________________________________Information of Employee_________________________________________")
print("________________________________________________________________________________________________")
print("{:<10} {:<10} {:<10} {:<10} {:<10} {:<10} {:<10} {:<10} {:<10}".format('CODE', 'NAME', 'GENDER', 'SALARY', 'HOURS', 'OT_HOURS', 'OT_RATE', 'DRPRE', 'TOTAL_SALARY'))
print("________________________________________________________________________________________________")
for employee in employees:
    print("{:<10} {:<10} {:<10} {:<10} {:<10} {:<10} {:<10} {:<10} {}$".format(*employee.values()))