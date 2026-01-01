# interest = 5% per year
# deposited sum into bank for 3 years

num = int(input())

first_year_sum = num * 1.05
second_year_sum = first_year_sum * 1.05
third_year_sum = second_year_sum * 1.05

format_year1 = round(first_year_sum, 2)
format_year2 = round(second_year_sum, 2)
format_year3 = round(third_year_sum, 2)

print(f"{format_year1:.2f}")
print(f"{format_year2:.2f}")
print(f"{format_year3:.2f}")