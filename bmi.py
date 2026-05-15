# Project : BMI Calculator

def main():
    print("===== BMI Calculator =====")

    # Input from user
    weight = float(input("Enter weight in kg: "))
    height = float(input("Enter height in meters: "))

    # BMI Formula
    bmi = weight / (height * height)

    # Display BMI
    print(f"\nYour BMI is: {bmi:.2f}")

    # BMI Status
    if bmi < 18.5:
        print("Status: Underweight")

    elif 18.5 <= bmi <= 24.9:
        print("Status: Normal Weight")

    elif 25 <= bmi <= 29.9:
        print("Status: Overweight")

    else:
        print("Status: Obese")


# Run Program
main()