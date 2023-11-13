# Get user input for height and weight
height = float(input("Enter your height in centimeters: "))
weight = float(input("Enter your weight in kg: "))

# Convert height to meters for BMI calculation
height = height / 100

# Calculate BMI
bmi = weight / (height * height)

# Print BMI result
print("Your Body Mass Index is:", bmi)

# Evaluate BMI and provide fun and descriptive feedback
if bmi > 0:
    if bmi <= 16:
        print("Oh no! You are severely underweight. Time to fuel up and gain some superhero strength!")
    elif bmi <= 18.5:
        print("You are underweight. How about embracing a balanced diet to boost your energy levels?")
    elif bmi <= 25:
        print("Congratulations! You are in the healthy BMI range. Keep up the good work!")
    elif bmi <= 30:
        print("Oops! You are overweight. No worries, a combination of healthy eating and exercise can do wonders!")
    else:
        print("Uh-oh! You are severely overweight. Time to embark on a fitness journey and be your healthiest self!")
else:
    print("Oops! Please enter valid details. Check that your height and weight are positive values.")
