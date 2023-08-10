
# Initialize variables
MilkStock = 1500
priceMilkStock = 37500  # price per case = $25
BeerStock = 3000
priceBeerStock = 60000  # price per case = $20
VitaStock = 2400
priceVitaStock = 7200  # price per case = $3

while True:
    # Display options
    print('--' * 20)
    print('\t\t1. Milk')
    print('\t\t2. Beer')
    print('\t\t3. Vita')
    print('--' * 20)
    option = int(input('\nChoose Option 1 - 2 or 3 (0 to quit): '))

    if option == 0:
        print('Exiting...')
        break  # Exit the loop

    if option in [1, 2, 3]:
        date = input('Input Buy Date (dd/mm/yy): ')
        quantity = int(input('Input Number of Product: '))

        # Calculate discount
        if quantity >= 10:
            discount = 10
        else:
            discount = 0

        print('Discount = $' + str(discount))
        price = float(input('Input Price per case : '))
        Total = (quantity * price) - discount
        print('Total = $' + str(Total))

        # Determine product details based on option
        if option == 1:
            product_name = 'Milk'
            product_stock = MilkStock
            price = priceMilkStock
        elif option == 2:
            product_name = 'Beer'
            product_stock = BeerStock
            price = priceBeerStock

        elif option == 3:
            product_name = 'Vita'
            product_stock = VitaStock
            price = priceVitaStock

        # Calculate total and remaining stock
        remaining_stock = product_stock - quantity

        # Display results
        print("\nResults:")
        print('--' * 60)
        print("{:<10} {:<15} {:<15} {:<15} {:<15} {:<15} {:<15} {:<15}".format(
            "Date", f"{product_name}(Stock)", "Total(Stock)", product_name, "Prices",
            "Discount", "Total(Sale)", f"{product_name}(Stock Remain)"))

        print("{:<10} {:<15} ${:<15} {:<15} ${:<15} ${:<15} ${:<15} {:<15}".format(
            date, product_stock, price, quantity, price, discount, Total, remaining_stock))

        print('\n')

    else:
        print('\nInvalid option! Choose again.')
