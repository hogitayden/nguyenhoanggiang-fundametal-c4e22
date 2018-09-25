h = float(input("Your height here! (in cm) "))
w = float(input("Your weight here! (in kg) "))
h = h/100
BMI = w/(h*h)
BMI = round(BMI,2)
print("Your BMI = ",BMI)

if BMI < 16:
    print("Severely underweight")
elif BMI < 18.5:
    print("Underweight ")
elif BMI < 25:
    print("Normal")
elif BMI < 30:
    print("Overweight")
else:
    print("Obese")