#Calculat how long tell weekend
print("The best days are the weekend broh! Lets find out how Many days are left tell we get to the weekend!")
name = input("My name is Al sort for algorithem, what is your name? ")
days_left = input(f"{name} there are 7 days in a week Sunday is number 1 & Saterday is number 7, what day is todays number? ")
days_left = int(days_left)

# def question():
#     days_left = input(f"{name} so remeber now there are 7 days in a week Sunday is number 1 & Saterday is number 7, so you can only input a number from 1-7 & no strings please... what is todays number in the week? ")
    # if days_left != 1 and days_left != 7 and days_left < 8:
    #     print(f"Ok I see so if it is day number {days_left} then we have {6 - days_left} day/days left tell the weekend!")
    # else:
    #     question()

if days_left != 1 and days_left != 7 and days_left < 8:
    print(f"Ok I see so if it is day number {days_left} then we have {6 - days_left} day/days left tell the weekend!")
else:
    # question()
    print("hmmm we are eather on the weekend or you did not put the right kind of input")