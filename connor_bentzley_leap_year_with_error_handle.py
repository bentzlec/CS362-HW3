import time

try:
    year = int(input("What year do you want to check? Enter: "))
except ValueError:
    print("Error! Please input an integer!")
    quit()


if (year % 4 == 0) and (year % 100 != 0):
    print(year, " is a leap year")
elif (year % 400 == 0):
    print(year, " is a leap year")
elif( ((year % 4 != 0) and (year % 100 != 0)) or (year % 400 != 0)):
    print(year, " is not a leap year")

time.sleep(50)