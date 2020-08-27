#Calculat how long tell weekend

#Greeting
print("The best days are the weekend broh! Lets find out how Many days are left tell we get to the weekend!")

#Ask for inputs
name = input("My name is Al sort for algorithem, what is your name? ")
days_left = input(f"{name} there are 7 days in a week Sunday is number 1 & Saterday is number 7, what day is todays number? ")
days_left = int(days_left)

#check input
if days_left != 1 and days_left != 7 and days_left < 8:
    print(f"Ok I see so if it is day number {days_left} then we have {6 - days_left} day/days left tell the weekend!")
else:
    print("hmmm we are eather on the weekend or you did not put the right kind of input")