#BMI Weight
Weight = float(input("Enter your Weight in kg:"))
Height = float(input("Enter your Height in meter:"))
BMI = Weight/ (Height * Height)
print(BMI)
if BMI <= 18.4:
    print("You are Underweight")
elif BMI >= 18.5 and BMI <= 24.9:
    print("You are Normal")
elif BMI >= 25.0 and BMI <= 39.9:
    print("You are Overweight")
else:
    print("You are Obese")
