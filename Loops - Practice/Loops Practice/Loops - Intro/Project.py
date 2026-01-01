# First solution

user_input = int(input())

print('1 - create, 2 - list, 3 - request, 0 - leave')

if user_input == 1 or user_input == 2  or user_input == 3 or user_input == 4:
    print('Doing {}')
elif user_input == 5:
    print("You have chosen to exit the program.")
else:
    print("Wrong command. Please enter a valid command.")


# Second one

while True:
    command = int(input('Enter a command (1 for create, 2 for list, 3 for request, 0 for leave):'))
    if command == 2:
        print('Doing list!')
    elif command == 3:
        print('Doing request!')
    elif command == 0:
        print('Thank you!')
        break
    elif command == 1:
        print('Doing create!')
        while True:
            print('Enter 01 for potato, 02 for fish, and 00 if you want to finish the order')
            product_code = input('Enter 2-digit product code or 00 to finish the order:')
            if product_code == '01':
                print('Adding potato to the order')
            elif product_code == '02':
                print('Adding fish to the order')
            elif product_code == '00':
                print('Order is finished')
                break
            else:
                print('Wrong code')
    else:
        print('Wrong. Please enter a valid command!')

# Third one

print('''Please enter a one digit command. Valid commands are: 
"1" for the command create order
"2" for the command list (orders)
"3" for the command request help 
"0" for the command leave or exit the program''')
 
# Create variable for the input. Notice the underscore after input.
input_ = ''
 
# Creating endless loop to handle th commands
while True:
    # We need to update/take the input from the user on each iteration
    input_ = input()
    # Now we have to check what is the input and act accordingly
    if input_ == '1':
        # Message for creating an order
        print('Enter 2 digit product code or 00 to finish the order')
        print('Enter 01 for potato, 02 for fish, and 00 if you want to finish the order')
 
        # Creating endless loop to handle adding the products to the order
        while True:
            # We need to update/take the input from the user on each iteration
            input_product_code = input()
            # Now we have to check what is the input and act accordingly
            if input_product_code == '01':
                print('Adding potato to the order')
            elif input_product_code == '02':
                print('Adding fish to the order')
            elif input_product_code == '00':
                print('The order is finished')
                # We need to exit this loop
                break
            # If none of the above was true then the code is not valid
            else:
                print('Wrong code')
 
    elif input_ == '2':
        print('Doing list command')
    elif input_ == '3':
        print('Doing request command')
    elif input_ == '0':
        print('Thank you')
        # We need to terminate the program
        break
    # If none of the above was true then the command is not valid
    else:
        print('Wrong command. Please enter a valid command!')