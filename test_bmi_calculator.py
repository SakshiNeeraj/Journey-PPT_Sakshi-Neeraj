import pandas as pd

def calculate_bmi(weight, height):
    # Calculate BMI
    bmi = round(weight / (height ** 2), 2)
    return bmi

def bmi_category(bmi):
    # Determine the BMI category
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 24.9:
        return "Normal weight"
    elif 25 <= bmi < 29.9:
        return "Overweight"
    else:
        return "Obese"

def test_bmi():
    # Read the test cases from the Excel file
    df = pd.read_excel('testcases.xlsx')
    
    passed_cases = []
    failed_cases = []

    for index, row in df.iterrows():
        weight = row['Weight']
        height = row['Height']
        expected_bmi = row['BMI']
        
        # Calculate the BMI
        calculated_bmi = calculate_bmi(weight, height)
        
        # Check if the calculated BMI matches the expected BMI
        if calculated_bmi == expected_bmi:
            passed_cases.append(index)
        else:
            failed_cases.append((index, expected_bmi, calculated_bmi))
    
    # Display the results
    print("Passed cases:", passed_cases)
    if failed_cases:
        print("Failed cases:")
        for case in failed_cases:
            print(f"Row {case[0]}: expected {case[1]}, got {case[2]}")

if __name__ == "__main__":
    test_bmi()
