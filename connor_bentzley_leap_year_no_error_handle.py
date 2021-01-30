import time

year = int(input("What year do you want to check? Enter: "))

if (year % 4 == 0) and (year % 100 != 0):
    print(year, " is a leap year")
elif (year % 400 == 0):
    print(year, " is a leap year")
else:
    print(year, " is not a leap year")

time.sleep(50)