import datetime
#constants
num_components = 6
components     = ['processor', 'ram', 'storage', 'screen', 'case', 'usb ports']
num_options    = 13
options        = ['p3', 'p5', 'p7', '16gb', '32gb', '1tb', '2tb', '23"', '19"', 'mini tower', 'midi tower', '2 ports', '4 ports']
option_nums   = [3, 2, 2, 2, 2, 2]
prices         = [100, 120, 200, 75, 150, 50, 100, 65, 120, 40, 70, 10, 20]
start_stock    = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10]

#variables
today_stock  = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10]
order_nums = []
orders_made  = 0
while True:
    order = []
    orders_made += 1
    options_index_start = 0
    for index in range(num_components):
        options_index_end = options_index_start + option_nums[index]
        choices = options[options_index_start:options_index_end]
        prompt  = 'what ' + components[index] + '? from: ' + ', '.join(choices) + '\n'
        choice = input(prompt)
        while choice not in choices:
            print('invalid option')
            choice = input(prompt)
        order.append(choice)
        options_index_start = options_index_end
    print('\nhere is a summary of your order:')
    print('component'.ljust(12), 'price ($)')
    total = 0
    for option in order:
        price = prices[options.index(option)]
        total += price
        print(option.ljust(12), price)
    estimate = int(total * 1.2)
    print(' '*12, '-'*5)
    print('total'.ljust(12), total)
    print('estimate (+20%)'.ljust(12), estimate)
    in_stock = True
    for item in order:
        if today_stock[options.index(item)] == 0:
            print(item, 'not in stock, could not complete order')
            in_stock = False
            break
    if not in_stock:
        break
    order_nums.append(estimate)
    for item in order:
        today_stock[options.index(item)] -= 1
    print('date:', datetime.datetime.now().strftime('%d-%m-%Y'))
    if input('\nis it end of day? ').lower().startswith('y'):
       break

print('\n\nend of day summary:')
print('\nmoney spent per order:')
for order_num in order_nums:
    print(order_num)
print('(', orders_made, 'orders in total', ')\n')
print('component'.ljust(19), 'no. sold')
for i in range(num_options):
    print(options[i].ljust(19), start_stock[i] - today_stock[i])
