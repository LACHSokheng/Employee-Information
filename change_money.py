print('---------------------------')
print('|\t1. Riels to Dollars')
print('|\t2. Dollars to Riels')
print('---------------------------')

while True:
    option = int(input('Choose Option 1 or 2: '))

    if option == 1:
        riels = float(input('Input Riels: '))
        rate = float(input('Input Rate : '))
        amountD = riels / rate
        print('Amount of (Dollars) : ${:.2f}'.format(amountD))
        continue  # Go back to the beginning of the loop to ask for input again

    else:
        dollar = float(input('Input Dollars: '))
        Exrate = float(input('Exchange Rate : '))
        amountRiel = dollar * Exrate
        print('Amount of (Riels): {:.2f}៛'.format(amountRiel))
        break  # Exit the loop after successful conversion


    # else:
    #     print('Invalid option. Please try again.')
    #     continue  # Go back to the beginning of the loop to ask for input again
