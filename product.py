# Option
print('--'*20)
print('1. Milk')
print('2. Beer')
print('3. Vita')
print('--'*20)

product = []

# ---------[ Create Fuction ]---------
# def Header():
#     print("\nResults:")
#     print("{:<10} {:<15} {:<5} {:<5} {:<5} {:<5} {:<5} {:<5}".format(
#         "Date", "Milk(Stock)", "Total(Stock)", "Milk", "Prices", "Discount", "Total(Sale)", "Milk(Stock Remain)"))
#     print("------------------------------------------------------------------------------")

MilkStock = 1500
priceMilkStock = 37500 # price per case = 25$
BeerStock = 3000
priceBeerStock = 60000 # price per case = 20$
VitaStock = 2400
priceVitaStock = 7200 # peice per case = 3$
discount = 0

while True:
    option = int(input('Choose Option 1 - 2 or 3: '))
    if option in [1, 2, 3]:
        date = input('Input Buy Date (dd/mm/yy): ')
        product = int(input('Input Number of Product: '))

        # I want to check dicount
        if (product >= 10):
            discount = 10
        else:
            discount = 0
        print('Discount = $' + str(discount))
        price = float(input('Input Price per case : '))
        Total = (product * price) - discount
        print('Total = $' + str(Total))

        if option == 1:
            product_name = 'Milk'
            # product_stock = MilkStock

            print("\nResults:")
            print('--' * 60)
            print("{:<10} {:<15} ${:<15} {:<15} {:<15} {:<15} {:<15} {:<15}".format(
                "Date", "Milk(Stock)", "Total(Stock)", "Milk", "Prices", "Discount", "Total(Sale)",
                "Milk(Stock Remain)"))

            print("{:<10} {:<15} {:<15} {:<15} ${:<15} ${:<15} ${:<15} {:<15}".format(
                date, MilkStock, priceMilkStock, product, price, discount, Total,MilkStock - product))

        elif option == 2:
            product_name = 'Beer'
            # product_stock = MilkStock

        elif option == 3:
            product_name = 'Vita'

        else:
            print('Choose again!')
