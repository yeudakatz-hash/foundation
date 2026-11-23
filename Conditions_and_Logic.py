# from foundations.types import salary
#
# #1
# age = int(input("Enter your age: "))
# if age >= 18:
#     print("Adult")
# else:
#     print("Minor")
#
#
#
# #2
# num = int(input("Enter a number: "))
# if num > 0:
#     print("Positive")
# elif num < 0:
#     print("Negative")
# else:
#     print("Zero")
#
#
#
# #3
# num = int(input("Enter a number: "))
# if num % 2 == 0:
#     print("Even")
# else:
#     print("Odd")
#
#
#
# #4
# n1 = int(input("Enter a number: "))
# n2 = int(input("Enter a number: "))
# if n1 > n2:
#     print("The number 1 is bigger!")
# elif n1 < n2:
#     print("The number 2 is bigger!")
# else:
#     print("The numbers are equal")
#
#
#
# #5
# password = "Python123"
# try_paasword = str(input("Enter a password: "))
# if password == try_paasword: print("access granted")
# else: print("access denied")
#
#
# #6
# num = int(input("Enter a number: "))
# if 0 < num < 11: print("single digit")
# elif 10 < num < 51: print("2 digit low")
# elif 50 < num < 101: print("2 digit high")
# else: print("out of range")
#
#
# #7
# num = int(input("Enter a grade: "))
# if 90 < num < 101: print("Excellent")
# elif 80 < num < 91: print("Very Good")
# elif 70 < num < 81: print("Good")
# elif 60 <= num < 71: print("Passed")
# elif 0 <= num < 60: print("Failed")
# else: print("Invalid Grade.")
#
#
# #8
# correct_username = "admin"
# correct_password = "123456"
# username = input("Enter your username: ")
# password = input("enter your password: ")
# if correct_password == password and correct_username == username:
#     print("Login Successful")
# elif username == correct_username:
#     print("Wrong Password")
# elif password == correct_password:
#     print("Unknown User")
# else:
#     print("Who are you???")
#
#
# #9
# age = int(input("Enter your age: "))
# if age > 60:
#     print("you have 20% discount")
# elif age < 18:
#     print("you have 10% discount")
# else:
#     print("you have not discount")
#
#
# #10
# num = int(input("Enter a number: "))
# if num % 3 == 0 and num % 5 == 0:
#     print("The number divide in 3 and 5")
# elif num % 3 == 0:
#     print("divide in 3")
# elif num % 5 == 0:
#     print("divide in 5")
# else:
#     print("Dont divide in 3 and 5")
#
#
# #11
# age = int(input("Enter your age: "))
# with_adult = input("enter if you with adult or not (T/F)")
# if age > 18 or age > 16 and with_adult == True:
#     print("You are welcome")
# else:
#     print("You can't get enter")
#
#
# #12
# avg = float(input("Enter a average of grades: "))
# salary = float(input("Enter a salary per month: "))
# if avg > 90 or (avg > 85 and salary < 5000):
#     print("Eligible for a scholarship")
#
#
# #13
# username = input("Enter your username: ")
# password = input("Enter your password: ")
# active_account = input("Enter if your account is activate (T/F)")
# if username == correct_username and password == correct_password and acctive_account:
#     print("you can enter")
#
#
# #14
# num = int(input("Enter a number: "))
# if 80 >= num >= 20:
#     print("The num in the range")
# if not num > 80 and not num < 20:
#     print("The num in the range")
#
#
# #15
# balance = 5000
# withdraw = float(input("Enter money to withdraw: "))
# if withdraw > 0:
#     if withdraw <= balance:
#         print("you can take your money")
#     else:
#         print("error")
# else:
#     print("you are strange")
#
#
# #16
# age = int(input("Enter your age: "))
# member_club = input("Enter if you are in club (T/F)")
# if age < 12:
#     price = 25
# elif age < 18:
#     price = 35
# else:
#     price = 50
# if member_club:
#     print(price * 0.9)
# else:
#     print(price)
#
#
#
# #17
# age = int(input("Enter your age: "))
# senior = int(input("enter your seniority: "))
# salary = int(input("Enter your salary: "))
# if age > 20:
#     if senior > 1:
#         if salary > 7000:
#             print("You can take loan")
#         else:
#             print("The salary is too low")
#     else:
#         print("your seniority is too low")
# else:
#     print("You are baby")
#
#
# #18
# vehicle = input("Enter your type vehicle: ")
# hours = float(input("Enter hours in parking: "))
# if vehicle == "motorcycle":
#     if hours < 1:
#         print((10 * hours) * 0.9)
#     elif hours > 5:
#         print((10 * hours) * 0.85)
#     else:
#         print(10 * hours)
# elif vehicle == "car":
#     if hours < 1:
#         print((20 * hours) * 0.9)
#     elif hours > 5:
#         print((20 * hours) * 0.85)
#     else:
#         print(20 * hours)
# elif vehicle == "truck":
#     if hours < 1:
#         print((30 * hours) * 0.9)
#     elif hours > 5:
#         print((30 * hours) * 0.85)
#     else:
#         print(30 * hours)
#

#19
n1 = int(input("Enter a number: "))
n2 = int(input("Enter a number: "))
action = input("Enter a action: ")
if action == "+":
    print(n1+n2)
elif action == "-":
    print(n1-n2)
elif action == "*":
    print(n1*n2)
elif action == "/":
    if n2 == 0:
        print("ZeroDivideError")
    else:
        print(n1/n2)
else:
    print("illegal operator")


#20
year = int(input("Enter a year: "))
if (year % 400 == 0) or (year % 4 == 0 and not year % 100 == 0):
    print("meuberet")
else:
    print("not meuberet")


#21
hours = int(input("Enter num of hours you work in last nonth: "))
salary = 50 * hours
if hours > 182:
    more_hours = hours - 182
    salary += more_hours * 50 * 0.25
    if more_hours > 2:
        salary += (more_hours - 2) * 50 * 0.25
print(salary)


#22
age = int(input("Enter your age: "))
price = float(input("Enter price you pay: "))
date = int(input("Enter date of shop: "))
member_club = input("Enter if you are in club (T/F)")
open_product = input("Enter if open the package (T/F)")
recept = input("Enter if you have recept (T/F)")
if not recept:
    print("You can't return the product because you haven't recept")
elif open_product:
    print("You can't return the product because you open the product")
elif price <= 0:
    print("The price can't be negative")
elif (date > 14 and not member_club) or  (date > 30 and member_club):
    print("You can't return the product because the time is passed")
