height = input("How tall are you? ")
weight = input("How much do you weigh? ")
BMI = float(weight)/(float(height)**2)
print(BMI)
if BMI < 18.5:
    print ("You are Underweight")
elif BMI < 15:
    print ("You are severely Underweight")
elif BMI > 18.5 and BMI < 25:
    print ("You are Normal weight")
elif BMI > 25 and BMI < 30:
    print ("You are Overweight")
elif BMI > 30:
    print ("You are Obese")
elif BMI > 35:
    print ("You are clinically Obese")