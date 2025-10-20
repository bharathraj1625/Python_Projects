print("welcome to the love calculator")
name_1 = input("what is your name ? : ")
name_2 = input("what is their name ? : ")

combined_string = name_1 + name_2
lower_case_string = combined_string.lower()
t = lower_case_string.count("t")
u = lower_case_string.count("u")
r = lower_case_string.count("r")
e = lower_case_string.count("e")

true = t + u + r + e 

l = lower_case_string.count("l")
o = lower_case_string.count("o")
v = lower_case_string.count("v")
e = lower_case_string.count("e")

love = l + o + v + e

love_score = int(str(true) + str(love))

if(love_score < 10) or (love_score > 90 ):
    print(f"your score is {love_score}, you go together like coke & mentos")
elif (love >= 40) and (love_score <= 50):
    print(f"your score is {love_score}, you are alreight together")
else :
    print(f"your score is {love_score}, you are not match")