'''
add_taxes = 0
total_bill = 0
add_txt_cost = 0
extra_txt_cost = 0
add_min_cost = 0
extra_min_cost = 0

if total_mins >= 60:
        add_min_cost = total_mins - 60
        add_txt_cost = total_txt_msg - 20
        extra_min_cost = add_min_cost * 0.10
        extra_txt_cost = add_txt_cost * 0.06
        total_extra_cost = extra_min_cost + extra_txt_cost
        add_taxes = total_extra_cost * 0.20
        total_bill = 12 + total_extra_cost + add_taxes

        if total_txt_msg >= 20:
            add_min_cost = total_mins - 60
            add_txt_cost = total_txt_msg - 20
            extra_min_cost = add_min_cost * 0.10
            extra_txt_cost = add_txt_cost * 0.06
            total_extra_cost = extra_min_cost + extra_txt_cost
            add_taxes = total_extra_cost * 0.20
            total_bill = 12 + total_extra_cost + add_taxes
    
        print(f'{add_txt_cost} additional messages for {extra_txt_cost:.2f} levas')
        print(f'{add_min_cost} additional minutes for {extra_min_cost:.2f} levas')
        print(f'{add_taxes:.2f} additional taxes')
        print(f'{total_bill:.2f} total bill')
else:
    print(f'{add_txt_cost} additional messages for {extra_txt_cost:.2f} levas')
    print(f'{add_min_cost} additional minutes for {extra_min_cost:.2f} levas')
    print(f'{add_taxes:.2f} additional taxes')
    print(f'{total_bill:.2f} total bill')
'''