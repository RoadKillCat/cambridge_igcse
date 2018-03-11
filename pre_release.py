import datetime

col_w_order = 15
col_w_sumry = 12

num_components = 6
num_choices    = 13
components     = ['processor', 'ram', 'storage', 'screen', 'case', 'usb ports']
choice_groups  = [3, 2, 2, 2, 2, 2]
choices        = ['p3',         'p5',         'p7', \
                  '16gb',       '32gb',             \
                  '1tb',        '2tb',              \
                  '23"',        '19"',              \
                  'mini tower', 'midi tower',       \
                  '2 ports',    '4 ports']
prices         = [100, 120, 200, 75, 150, 50, 100, 65, 120, 40, 70, 10, 20]
start_stock    = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10]

today_stock  = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10]
order_nums   = []
orders_made  = 0
end_of_day = False

while not end_of_day:
    order = []
    choices_index_start = 0
    for index in range(num_components):
        choices_index_end = choices_index_start + choice_groups[index]
        possible_choices = choices[choices_index_start:choices_index_end]
        prompt  = 'what ' + components[index] + '? from: ' + ', '.join(possible_choices) + '\n'
        choice = input(prompt)
        while choice not in possible_choices:
            print('invalid choice')
            choice = input(prompt)
        order.append(choice)
        choices_index_start = choices_index_end
    print('\nhere is a summary of your order:')
    print('component'.ljust(col_w_order), 'price ($)')
    total = 0
    for choice in order:
        price = prices[choices.index(choice)]
        total += price
        print(choice.ljust(col_w_order), price)
    estimate = int(total * 1.2)
    print(' '*col_w_order, '-'*5)
    print('total'.ljust(col_w_order), total)
    print('estimate (+20%)'.ljust(col_w_order), estimate, '\n')

    in_stock = True
    for choice in order:
        if today_stock[choices.index(choice)] == 0:
            print(item, 'not in stock, could not complete order')
            in_stock = False
    if not in_stock:
        continue
    order_nums.append(estimate)
    orders_made += 1
    for choice in order:
        today_stock[choices.index(choice)] -= 1
    print('date:', datetime.datetime.now().strftime('%d-%m-%Y'))
    if input('\nis it end of day? ').lower().startswith('y'):
        end_of_day = True

print('\n\nend of day summary:')
print('\nmoney spent per order:')
for order_num in order_nums:
    print(order_num)
print('(', orders_made, 'orders in total', ')\n')
print('component'.ljust(col_w_sumry), 'no. sold')
for index in range(num_choices):
    print(choices[index].ljust(col_w_sumry), 
          start_stock[index] - today_stock[index])
