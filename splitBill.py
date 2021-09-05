# program will calculate how a bill(amount) can be slit
bill_total = float(input("Total bill amount: R"))
split = int(input("How many people are splitting the bill? "))
tip_percentage = float(input("How much would you like to tip? 5%, 10% or 15% ? "))

tip_percentage /= 100
tip_amount = bill_total * tip_percentage
total = bill_total + tip_amount
bill_split = total / split

print("-------   ------\nBill total (incl. tip): R",total,"\nEach person pays: R",bill_split)
