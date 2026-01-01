month = input()
date = int(input())

if month == 'March' and date >= 20 or month == 'April' or month == 'May' or month == 'June' and date < 21:
    print('Spring')
elif month == 'June' and date >= 21 or month =='July' or month == 'August' or month == 'September' and date < 22:
    print('Summer')
elif month == 'September' and date >= 22 or month == 'October' or month == 'November' or month == 'December' and date < 30:
    print('Autumn')
elif month == 'December' and date >= 21 or month == 'January' or month == 'February' or month == 'March' and date < 20:
    print('Winter')