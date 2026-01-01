total_txt_msg = int(input())
total_mins = int(input())

add_taxes = 0.0
total_bill = 0

if total_txt_msg > 20: # input: msg = 31 ; mins = 115
    extra_msg = total_txt_msg - 20
    extra_msg_cost = extra_msg * 0.06
else:
    extra_msg = 0
    extra_msg_cost = 0.00

add_taxes += extra_msg_cost

print(f"{extra_msg} additional messages for {extra_msg_cost:.2f} levas")

if total_mins > 60:
    extra_mins = total_mins - 60
    extra_mins_cost = extra_mins * 0.10
else:
    extra_mins = 0
    extra_mins_cost = 0.00

add_taxes += extra_mins_cost

print(f'{extra_mins} additional minutes for {extra_mins_cost:.2f} levas')

sales_tax = add_taxes * 0.20
print(f'{sales_tax:.2f} additional taxes')

total_bill = add_taxes + sales_tax + 12
print(f'{total_bill:.2f} total bill')