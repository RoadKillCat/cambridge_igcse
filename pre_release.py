import datetime
components = ['Processor p3', 'Processor p5', 'Processor p7', 'RAM 16GB', 'RAM 32GB', 'Storage 1TB', 'Storage 2TB', 'Screen 23"', 'Screen 19"', 'Case Mini Tower', 'Case Midi Tower', 'USB ports 2 ports', 'USB ports 4 ports']
prices = [100, 120, 200, 75, 150, 50, 100, 65, 120, 40, 70, 10, 20]
start_stock = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10]
today_stock = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10]
orders = []

print('\033[4mComputer Shop\033[0m\n');
print('We have the following components:')
print('\n'.join(components))
while True:
    order = []
    print('\nWhat would you like to buy?\nEnter one per line, followed by STOP')
    item = input()
    while item != 'STOP':
        if item in components:
            order.append(item)
        else:
            print('Sorry we do not have that component!')
        item = input()
    print('\nHere is a summary of your order:')
    print('Component'.ljust(19), 'Price ($)')
    total = 0
    for item in order:
        price = prices[components.index(item)]
        total += price
        print(item.ljust(19), price)
    estimate = int(total * 1.2)
    print(' '*19, '-'*5)
    print('Total'.ljust(19), total)
    print('Estimate (+20%)'.ljust(19), estimate)
    in_stock = True
    for item in order:
        if not today_stock[components.index(item)]:
            print('Sorry,', item, 'is not in stock, so could not complete order')
            in_stock = False
            break
    if not in_stock:
        break
    for item in order:
        today_stock[components.index(item)] -= 1
    orders.append(estimate)
    print('The date is', datetime.datetime.now().strftime('%d-%m-%Y'))
    if input('\nIs it the end of the day? ').lower().startswith('y'):
       break;

print('\nEnd of Day Summary:')
print('\nAmount of money spent per order:')
for order in orders:
    print(order)
print('(', len(orders), 'orders in total', ')\n')
print('Component'.ljust(19), 'No. Sold')
for i in range(13):
    print(components[i].ljust(19), start_stock[i] - today_stock[i])
print('Goodnight')
