bill = float(input("How much is the bill?"))
tip = float(input("What percentage tip would you like to give?"))
people = int(input("How many people are you splitting the bill with?"))

total = (bill * tip) % people

print(f"Your total is {total}. Thanks for using the tip calculator!")