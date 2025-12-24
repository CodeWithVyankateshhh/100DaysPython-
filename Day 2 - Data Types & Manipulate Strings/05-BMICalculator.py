print("Welcome to BMI Calculator")
# bmi range


height = float(input("Enter Your height(cm): "))

Weight = float(input("Enter Your Weight(kg): = "))

# BMI = weight (kg) / height (m) ^2.

height = height / 100  # converting cm to meter

Bmi = Weight / (height*height)

print("Your BMI is", round(Bmi,2))
if Bmi < 18.5:
  print("Your are Underweight")
elif Bmi < 24.9:
  print("You have Normal Weight")
elif Bmi < 29.9:
  print("You are Overweight")
else:
  print("Obesity")



# print("BMI Categories:")
# print("Underweight = <18.5")
# print("Normal weight = 18.5–24.9")
# print("Overweight = 25–29.9")
# print("Obesity = BMI of 30 or greater")
