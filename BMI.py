# get the Body Mass Index
# BMI = weight (kg) / height ^2 (h**2)

weight = float(input("Please enter the weight (kg): "))
height = float(input("Please enter the height (m): "))

bmi = weight / (height**2)

print("The BMI(Body Mass Index is: ",bmi)