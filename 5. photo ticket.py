print("welome to roller coaster")
height=int(input("what is your height in cm : "))

bill=0

if height >= 120:
    print("you can ride the roller coaster")
    age = int(input("what is your age : "))
    if age < 12:
        bill=5
        print("child tickets are $5")
    elif age <= 18:
        bill=7
        print("youth tickets are $7")
    else :
        bill=12
        print("adult tickets are $12")

want_photo = input("do you want photo take ? yes or no  :")

if want_photo == "yes":
    bill +=3
    print(f"your total bill is ${bill}")
else:
    print(f"sorry you have to grow taller")
