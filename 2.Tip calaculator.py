print("welcome to tip calculator")
bill=float(input("what was the bill : $"))
tip=int(input("how much tip would you like to give? 10, 20, or 30 : "))
people=int(input("how many people to split the bill ? : "))
tip_as_present=tip/100
total_tip_amount=bill*tip_as_present
total_bill=bill+total_tip_amount
bill_per_person=total_bill/people
final_amount=round(bill_per_person,2)
final_amount="{:.2f}".format(bill_per_person)
print(f"each person should pay ${final_amount}")
