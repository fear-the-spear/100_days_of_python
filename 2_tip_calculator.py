# Day 2 - Tip Calculator
print("Welcome to the tip calculator.")

total = input("What was the total bill? $")
total_as_float = round(float(total), 2)

tip = input("What percentage tip would you like to give? 10, 12, 15, or 20: ")
tip_as_float = round(float(tip), 2)
tip_as_percentage = (tip_as_float * .01) + 1

parties = input("How many people are splitting the bill? ")
parties_as_int = int(parties)

split_total = round((tip_as_percentage * total_as_float) / parties_as_int, 2)
formatted_split_total = "{:.2f}".format(split_total)
print(f"Each person should pay ${formatted_split_total}")