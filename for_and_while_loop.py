
# 1
i = 1
while i <= 10:
    print(i)
    i += 1


# 2
i = 10
while i > 0:
    print(i)
    i -= 1
print("START!")


# 3
i = 1
while i <= 50:
    if i % 2 == 0:
        print(i)
    i += 1


# 4
num = int(input("Enter a number: "))
i = 1
while i <= 5:
    print(num * i)
    i += 1


# 5
count = 0
i = 1
while i <= 100:
    count += i
    i += 1
print(count)


# 6
secret_password = "Python123"
your_password = input("Enter your password: ")
while not your_password == secret_password:
    your_password = input("Enter your password: ")
print("Welcome!")


# 7
secret_number = 27
your_password = input("Enter your password: ")
while not your_password == secret_password:
    your_password = input("Enter your password: ")
print("Welcome!")



# 8
count = 0
choose = input("Enter a number: ")
while choose != 0:
    count += choose
    choose = input("Enter a number: ")
print(choose)


# 9
counter = 0
sum_grades = 0
grade = int(input("Enter a grade: "))
while grade!= 999:
    sum_grades += grade
    counter += 1
    grade = int(input("Enter a grade: "))
print(f"the sum of grades is {sum_grades} and the avg is {sum_grades/ counter}")


# 10
counter = 0
sum_positive = 0
num = int(input("Enter a number: "))
while num >= 0:
    sum_positive += num
    counter += 1
    num = int(input("Enter a number: "))
print(f"you enter  {counter} numbers and the sum of all them is {sum_positive}")


# 11
num = int(input("Enter a number: "))
i = 1
while i <= 10:
    print(f"{num} * {i} = {num * i}")
    i += 1


# 12
num = int(input("Enter a number: "))
counter = 0
while num > 0:
    counter += 1
    num //= 10
print(counter)


# 13
num = int(input("Enter a number: "))
new_num = 0
while num > 0:
    new_num = new_num * 10 + num % 10
    num = num // 10
print(new_num)


# 14
num = int(input("Enter a number: "))
i = 2
while i < num ** 0.5:
    if num % i == 0:
        print("not rishoni")
        break
    else:
        i += 1



# 15
balance = 5000
print("""
1. Check balance
2. Deposit money
3. Withdraw money
4. Log out
""")
choose = int(input("Enter a choice: "))
while choose != 4:
    if choose == 1:
        print(balance)
    elif choose == 2:
        balance += int(input("enter sum to deposit: "))
    elif choose == 3:
        withdraw = int(input("Enter num to withdraw: "))
        if withdraw > balance:
            print("The withdraw more than balance")
        else:
            balance -= withdraw
    print("""
    1. Check balance
    2. Deposit money
    3. Withdraw money
    4. Log out
    """)
    choose = int(input("Enter a choice: "))



# 16
i = 1
while True:
    print(i)
    if i == 15:
        break
    i += 1


# 17
i = 0
while i < 30:
    i += 1
    if i % 3 == 0:
        continue
    print(i)


# 18
while True:
    num = int(input("Enter a number: "))
    if num == 100:
        print("Success!")
        break


# 19
for i in range(1,21):
    print(i)


# 20
for i in range(1, 21):
    print(i * 5)


# 21
count = 0
for i in range(101):
    count += i
print(count)


# 22
num = int(input("Enter a number: "))
for i in range(1, num + 1):
    print(f"{num} * {i} = {num * i}")


# 23
n1 = int(input("Enter a number: "))
n2 = int(input("Enter a number: "))
mi = min(n1, n2)
ma = max(n1, n2)
count = 0
for i in range(mi, ma + 1):
    count += i
print(count)


# 24
for i in range(101):
    if i % 3 == 0 and i % 5 == 0:
        print(i)


# 25
row = int(input("Enter a row: "))
column = int(input("Enter a column: "))
for i in range(row):
    for j in range(column):
        print("*", end="")
    print()
    j = 0


# 26
row = int(input("Enter a row: "))
for i in range(row + 1):
    for j in range(i):
        print("*", end="")
    print()
    j = 0


# 27
for i in range(1,11):
    for j in range(1,11):
        print(i * j,"  ", end="")
    j = 0
    print()


# 28
for i in range(1,6):
    for j in range(1, 6):
        print(i , j)
    j = 0


# 29
res = 0
while True:
    choose = int(input("""
    ===== MATH GAME =====

    1. Start Game
    2. View Instructions
    3. Exit

    Choose:
    """))
    if choose == 1:
        res = 0
        j = 5
        for i in range(11, 21):
            print(i ," * ", j)
            result  = int(input("Enter your result: "))
            if i * j == result:
                res += 1
    if choose == 2:
        print(res)
    if choose == 3:
        break




