# program will calculate how a bill(amount) can be slit

bill_total = float(input("Total bill amount: R"))   # total of the bill
split = int(input("How many people are splitting the bill? "))  # how many way splitting it
tip_percentage = float(input("How much would you like to tip? 5%, 10% or 15% ? "))  # tip

tip_percentage /= 100   # convert to decimal
tip_amount = bill_total * tip_percentage    # get the new total with tip included
total = bill_total + tip_amount # add tip to the bill total
bill_split = round(total / split , 2)   # split the bill -> rounded to 2 decimal places

print(f"-------   ------\nBill total (incl. tip): R{total}\nEach person pays: R{bill_split}")
