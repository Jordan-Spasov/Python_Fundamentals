# First solution

#Input
#1:00 PM

#Output

#beer time

"""t_format_input = input()

if t_format_input >= 1:00 and t_format_input <= 00:00:
    print("beer time")
elif t_format_input >= 3:00 and t_format_input <= 00:00:
    print("non-beer time")
else:
    print("invalid time")"""

# Second solution

# Step 1: Read input and check format (must contain " "(space) and ":"(semicolon))
time_str = input().strip()

if " " not in time_str or ":" not in time_str:
    print("invalid time")
else:
    # Step 2: Split into time and AM/PM
    time_part, am_pm = time_str.split(" ")

    if am_pm != "AM" and am_pm != "PM":
        print("invalid time")
    else:
        # Step 3: Split into hour and minutes
        hour_minute = time_part.split(":")

        if len(hour_minute) != 2:
            print("invalid time")
        else:
            hour, minute = hour_minute

            # Step 4: Validate digits
            if not hour.isdigit() or not minute.isdigit():
                print("invalid time")
            else:
                hour = int(hour)
                minute = int(minute)

                # Step 5: Validate hour and minute range
                if hour < 1 or hour > 12:
                    print("invalid time")
                elif minute < 0 or minute > 59:
                    print("invalid time")
                else:
                    # Step 6: Convert to 24-hour format
                    if am_pm == "PM" and hour != 12:
                        hour += 12
                    if am_pm == "AM" and hour == 12:
                        hour = 0

                    # Step 7: Check if it is beer time
                    if (hour >= 13 and hour < 24) or (hour >= 0 and hour < 3):
                        print("beer time")
                    else:
                        print("non-beer time")


# Third solution
                        given_time = "0:52 AM"
# given_time = input()

if " " in given_time and ":" in given_time:
    time_as_digit, slot = given_time.split()
    hour, minutes = time_as_digit.split(":")

    if hour.isdigit() and minutes.isdigit() and 0 <= int(hour) <= 12 and 0 <= int(minutes) <= 59 and slot == "PM":
        hour = int(hour) + 12
        if 13 <= hour <= 24:
            print("beer time")
        else:
            print("non-beer time")

    elif hour.isdigit() and minutes.isdigit() and 0 <= int(hour) <= 12 and 0 <= int(minutes) <= 59 and slot == "AM":
        if 3 <= int(hour) and int(hour) != 12:
            print("non-beer time")
        else:
            print("beer time")
    else:
        print("invalid time")

else:
    print("invalid time")