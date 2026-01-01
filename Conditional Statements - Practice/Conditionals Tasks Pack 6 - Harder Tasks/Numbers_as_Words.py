# Input

# 0
# Output

# zero

num = int(input())

if num == 0:
    print("zero")
else:
    hundreds = num // 100
    tens = (num - (hundreds * 100)) // 10
    ones = num - (hundreds * 100) - (tens * 10)

    output_for_hundreds = ""
    output_for_tens = ""
    output_for_ones = ""

    if ones > 0 and tens != 1:
        if ones == 1:
            output_for_ones = "one"
        elif ones == 2:
            output_for_ones = "two"
        elif ones == 3:
            output_for_ones = "three"
        elif ones == 4:
            output_for_ones = "four"
        elif ones == 5:
            output_for_ones = "five"
        elif ones == 6:
            output_for_ones = "six"
        elif ones == 7:
            output_for_ones = "seven"
        elif ones == 8:
            output_for_ones = "eight"
        elif ones == 9:
            output_for_ones = "nine"

    if tens >= 2:
        if tens == 2:
            output_for_tens = "twenty"
        elif tens == 3:
            output_for_tens = "thirty"
        elif tens == 4:
            output_for_tens = "forty"
        elif tens == 5:
            output_for_tens = "fifty"
        elif tens == 6:
            output_for_tens = "sixty"
        elif tens == 7:
            output_for_tens = "seventy"
        elif tens == 8:
            output_for_tens = "eighty"
        elif tens == 9:
            output_for_tens = "ninety"

        if output_for_ones != "":
            output_for_tens += " "

    if tens == 1:
        if ones == 0:
            output_for_tens = "ten"
        elif ones == 1:
            output_for_tens = "eleven"
        elif ones == 2:
            output_for_tens = "twelve"
        elif ones == 3:
            output_for_tens = "thirteen"
        elif ones == 4:
            output_for_tens = "fourteen"
        elif ones == 5:
            output_for_tens = "fifteen"
        elif ones == 6:
            output_for_tens = "sixteen"
        elif ones == 7:
            output_for_tens = "seventeen"
        elif ones == 8:
            output_for_tens = "eighteen"
        elif ones == 9:
            output_for_tens = "nineteen"

        output_for_ones = ""

    if hundreds > 0:
        if hundreds == 1:
            output_for_hundreds = "one hundred"
        elif hundreds == 2:
            output_for_hundreds = "two hundred"
        elif hundreds == 3:
            output_for_hundreds = "three hundred"
        elif hundreds == 4:
            output_for_hundreds = "four hundred"
        elif hundreds == 5:
            output_for_hundreds = "five hundred"
        elif hundreds == 6:
            output_for_hundreds = "six hundred"
        elif hundreds == 7:
            output_for_hundreds = "seven hundred"
        elif hundreds == 8:
            output_for_hundreds = "eight hundred"
        elif hundreds == 9:
            output_for_hundreds = "nine hundred"

        if output_for_tens != "" or output_for_ones != "":
            output_for_hundreds += " and "

    print(output_for_hundreds + output_for_tens + output_for_ones)