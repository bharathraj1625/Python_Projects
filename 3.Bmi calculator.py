height=float(input("enter your hieghtin m :"))
weight=float(input("enter your weight : "))

bmi=round(weight/height**2)

if bmi < 18.5:
    print(f"your bmi is {bmi}, you are underwight")
elif bmi < 25:
    print(f"your bmi is {bmi}, you are normal weight")
elif bmi < 30:
     print(f"your bmi is {bmi}, you are slightly overweight")
elif bmi < 35:
    print(f"your bmi is {bmi}, you are obese")
else :
    print(f"your bmi is {bmi}, you are elinically obese")