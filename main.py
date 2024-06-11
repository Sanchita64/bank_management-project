name = str(input("Enter your name: "))

weight = float(input("Enter your weight in kgs: "))

height = float(input("Enter your height in metres: "))

BMI = (weight) / (height)

print("The BMI is: ", BMI)
if BMI > 0:
    if (BMI < 16):
        print("The person is severely thin.")
    
    elif (BMI < 17):
        print("The person is moderately thin.")
    
    elif (BMI < 18.5):
        print("The person is mild thin.")
    
    elif (BMI < 25):
        print("The person is normal.")
    
    elif (BMI < 30):
        print("The person is overweight.")
    
    elif (BMI < 35):
        print("The person comes in Obese Class I.")
    
    elif (BMI <40):
        print("The person comes in Obese Class II.")
    
    else:
        print("The person comes in Obese Class III.")

else:
    print("Invalid input.")
    




