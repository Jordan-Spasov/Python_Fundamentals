products = [
    '01.Potato',
    '02.Fish',
    '03.Apple',
    '04.Orange'
]

order_num = []
help_req = []

while True:
    command = input('Enter a command (Order, List orders, Request help, Leave): ')
    if command == 'Order':
        order_items = []
        print('Available products:')
        for product in products:
            print(product)
        while True:
            product_code = input('Enter product code (or "0" to finish): ')
            if product_code == '0':
                break
            order_items.append(product_code)
        if order_items:
            order_num.append(' '.join(order_items))
            print('Order added.')
        else:
            print('Empty order not saved.')

    elif command == 'List orders':
        if not order_num:
            print('You have no orders.')
        else:
            print('Here are your orders:')
        for index, order in enumerate(order_num, start = 1):
            print(f'{index}. {order}')

            if order.number.isdigit():
                order_index = int(order.number) - 1
                if 0 <= order_index < len(order_num):
                    help_req.append(order_num)
                    print(f'Help request added for order {order_num}.')
                else:
                    print('Invalid order number.')
            else:
                print('Invalid order number.')

    elif command == 'Leave':
        print('Thank you for using our program!')
        print('Summary of your interaction:')

        if order_num:
            print('Orders places:')
            for index, order in enumerate(order_num, start = 1):
                print(f'{index}. {order}')
        else:
            print('No orders placed.')
        
        if help_req:
            print('Help requested for orders:", ", " '.join(help_req))
        else:
            print('No help requests made.')
        break
    else:
        print('Invalid command. Please try again.')