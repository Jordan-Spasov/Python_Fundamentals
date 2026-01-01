price = float(input())
pay_lv = float(input())

price = round(price * 100)
pay_lv = round(pay_lv * 100)
change = pay_lv - price

if change // 100 > 0:
    count = change // 100
    change -= count * 100
    print(f"{count} x 1 lev")
if change // 50 > 0:
    count = change // 50
    change -= count * 50
    print(f"{count} x 50 stotinki")
if change // 20 > 0:
    count = change // 20
    change -= count * 20
    print(f"{count} x 20 stotinki")
if change // 10 > 0:
    count = change // 10
    change -= count * 10
    print(f"{count} x 10 stotinki")
if change // 5 > 0:
    count = change // 5
    change -= count * 5
    print(f"{count} x 5 stotinki")
if change // 2 > 0:
    count = change // 2
    change -= count * 2
    print(f"{count} x 2 stotinki")
if change // 1 > 0:
    count = change // 1
    change -= count * 1
    print(f"{count} x 1 stotinka")