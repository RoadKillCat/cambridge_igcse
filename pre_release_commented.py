#import library so we have access to the date
import datetime

#printing
#width of the columns for the order printout
col_w_order = 15
#width of the columns for the summary table
col_w_sumry = 12

#constants
#how many components are there?
num_components = 6
#how many choices are there altogether?
num_choices    = 13
#what are the components?
components     = ['processor', 'ram', 'storage', 'screen', 'case', 'usb ports']
#how many choices are in each group?
#(e.g. 3 different processors)
choice_groups  = [3, 2, 2, 2, 2, 2]
#what are all the choices?
choices        = ['p3',         'p5',         'p7', \
                  '16gb',       '32gb',             \
                  '1tb',        '2tb',              \
                  '23"',        '19"',              \
                  'mini tower', 'midi tower',       \
                  '2 ports',    '4 ports']
#how much does each choice cost?
prices         = [100, 120, 200, 75, 150, 50, 100, 65, 120, 40, 70, 10, 20]
#stock at the start of the day, we can then subtract from this the
#stock at the end of the day to get the sales
start_stock    = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10]

#variables
#what is the running stock?
today_stock  = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10]
#list to keep track of the estimate numbers
order_nums   = []
#counter holding how many orders have been made today
orders_made  = 0
#boolean representing if it is the end of the day
end_of_day = False

#this is the main customer loop, whilst it is day time, keep accepting customers
while not end_of_day:
    #TASK 1
    #initialise a list to store the choices made
    order = []
    #the index of the start of the current component choices
    choices_index_start = 0
    #iterate over the indexes for each choice
    for index in range(num_components):
        #calculate the index of the end of the current component choices
        choices_index_end = choices_index_start + choice_groups[index]
        #retrieve the possible choices that can be made for this component from choices
        possible_choices = choices[choices_index_start:choices_index_end]
        #generate the prompt: "what _component_? from a, b, c"
        prompt  = 'what ' + components[index] + '? from: ' + ', '.join(possible_choices) + '\n'
        #ask the user
        choice = input(prompt)
        #loop whilst there input is invalid (i.e. not in choices)
        while choice not in possible_choices:
            #print that the input was invalid
            print('invalid choice')
            #ask again
            choice = input(prompt)
        #append what they chose to the order
        order.append(choice)
        #the start of the next group of choices is now the current end index
        choices_index_start = choices_index_end
    #print them a summary
    print('\nhere is a summary of your order:')
    #using .ljust to display a neat table
    print('component'.ljust(col_w_order), 'price ($)')
    #whilst printing out their choices, also total up the price of their components
    #the total is initially 0
    total = 0
    #iterate over their choices
    for choice in order:
        #retrieve how much that choice cost by finding its index and getting
        #the element of the same index from the prices list
        price = prices[choices.index(choice)]
        #add the price to the total
        total += price
        #print the choice to the table, with the price 
        print(choice.ljust(col_w_order), price)
    #the estimate is the 120%, so multiply by 1.2 and convert to int
    estimate = int(total * 1.2)
    #output the total and the estimate to the table
    print(' '*col_w_order, '-'*5)
    print('total'.ljust(col_w_order), total)
    print('estimate (+20%)'.ljust(col_w_order), estimate, '\n')

    #TASK 2
    #begin by saying that all the choices are in stock
    in_stock = True
    #iterate over each of their choices
    for choice in order:
        #check whether there are none left
        if today_stock[choices.index(choice)] == 0:
            #print appropritate message
            print(item, 'not in stock, could not complete order')
            #in_stock is now False as there is none of something
            in_stock = False
    #if something was not in stock
    if not in_stock:
        #jump to the next iteration of the loop, i.e. next customer
        continue
    #the order is now valid, so can proceed with confirmation
    #add their estimate number to our list of order numbers
    order_nums.append(estimate)
    #increment the number of orders made
    orders_made += 1
    #iterate over each of their choices again to adjust stock levels
    for choice in order:
        #decrement the stock level for that choice
        today_stock[choices.index(choice)] -= 1
    #finalise the order with the date
    print('date:', datetime.datetime.now().strftime('%d-%m-%Y'))
    #ask if it is the end of the day and check if the lowercase version of
    #their answer starts with a 'y' (for 'yes')
    if input('\nis it end of day? ').lower().startswith('y'):
        #it is now the end of day, so set to true to escape the customer loop
        end_of_day = True

#TASK 3
#print a title
print('\n\nend of day summary:')
#print heading to say that the next numbers are the money spent numbers
print('\nmoney spent per order:')
#iterate over each order number
for order_num in order_nums:
    #print it
    print(order_num)
#print how many orders were made - simply the variable
print('(', orders_made, 'orders in total', ')\n')
#print a table of the amount of each component sold
print('component'.ljust(col_w_sumry), 'no. sold')
#iterate over the indexes of the choices
for index in range(num_choices):
    #print out that component and the difference between the stock at the start of the
    #day and the stock at the end of the day (today_stock) - this is how many were sold
    print(choices[index].ljust(col_w_sumry), 
          start_stock[index] - today_stock[index])
