

#1
numbers = [10,20,30,40,50]
print(numbers)
print(numbers[0])
print(numbers[-1])
print(numbers[2])


#2
names = ["Avi", "Gad", "Dani", "Dana"]
print(len(names))
print(names[0], names[-1])
names[1] = "Shay"
print(names)


#3
grades = [90, 80, 70, 60, 50]
grades.append(40)
grades.insert(0, 100)
grades[2] = 81
print(grades)


#4
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
numbers.remove(1)
print(numbers)
numbers.pop()
print(numbers)
numbers.pop(2)
print(numbers)


#5
products = ["computer", "keyboard", "mouse", "banana"]
print("mouse" in products)
print("batata" in products)


#6
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for i in numbers:
    print(numbers[i - 1])


#7
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for i in numbers:
    if numbers[i - 1] % 2 == 0:
        print(numbers[i - 1])


#8
grades = [90, 80, 70, 60, 50]
count = 0
for i in grades:
    count += i
print(count)


#9
numbers = [1, 2, 3, 4, 5, 15, 7, 8, 9, 10]
ma = numbers[0]
for i in numbers:
    if i > ma:
        ma = i
print(ma)


10
names = ["Avi", "Gad", "Dani", "Dana"]
name = input("Enter your name: ")
found = False
for i in names:
    if name == i:
        found = True
        print("Found")
if found is False:
    print("Not Found")


11
numbers = [10, 2, 3, 4, 5, 3, 7, 8, 9, 10]
num = int(input("Enter a number: "))
found = []
for i in range(len(numbers)):
    if num == numbers[i]:
        found.append(i)
print(found)


#12
count = 0
numbers = [100, 20, 30, 4, 15, 13, 70, 8, 19, 10]
for i in numbers:
    if i > 50:
        count += 1
print(count)


#13
numbers = [100, 20, 30, 4, 15, 13, 70, 8, 19, 10]
evens = []
for i in numbers:
    if i % 2 == 0:
        evens.append(i)
print(evens)


#14
names = ["Avi", "Gad", "Dani", "Dana"]
counter = 0
while names:
    counter += 1
    print(counter, names[0])
    names.pop(0)


#15
numbers = [10, 50, 20, 40, 70, 90, 35, 84, 15, 73]
print(numbers[:3])
print(numbers[-3:])
print(numbers[2:7])
print(numbers[::-1])


#16
names = ["Avi", "Gad", "Dani", "Dana", "Shany", "Shir", "Shay", "Ron", "Tal", "Yam"]
for i in range(len(names)):
    if i % 2 == 0:
        print(names[i], end="  ")
print()
for i in range(len(names)):
    if i % 2 == 1:
        print(names[i], end="  ")
print()
print(names[::-2])


#17
numbers = [10, 50, 5, 99, 20, 40, 70, 90, 35, 84, 14, 85, 94, 47, 72, 27, 82, 1, 15, 73]
numbers1 = numbers[:10]
numbers2 = numbers[10:]
numbers3 = numbers[4:14]


#18
numbers = [10, 50, 5, 99, 20, 40, 70, 90, 35, 84, 14, 85, 94, 47, 72, 27, 82, 1, 15, 73]
numb1 = numbers[:int(len(numbers) / 2)]
numb2 = numbers[int(len(numbers) / 2):]


#19
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
new_list1 = [n * 2 for n in numbers]
new_list2 = [n ** 2 for n in numbers]
new_list3 = [n for n in numbers if n % 2 == 0]
new_list4 = [n for n in numbers if n > 5]


#20
grades = [55, 90, 67, 100, 45, 82, 73, 30]
new_grades1 = [g for g in grades if g > 60]
new_grades2 = [g for g in grades if g < 60]
new_grades3 = [g + 5 for g in grades]


#21
names = ["Moshe", "David", "Dana", "Noa", "Michael", "Avi"]
new_names1 = [n for n in names if len(n) > 4]
new_names2 = [n.upper() for n in names]
new_names3 = [n for n in names if n.startswith("D")]


#22
numbers = [12, 7, 25, 30, 9, 44, 18, 3]
nu = [n for n in numbers if n % 3 == 0 and n > 10]


#23
li = []
for i in range(10):
    li.append(int(input("Enter a number: ")))
minimum = li[0]
maximum = li[0]
count = 0
for i in li:
    if i > maximum:
        maximum = i
    elif i < minimum:
        minimum = i
    count += i
print(minimum, maximum, count)


#24
names = ["Avi", "Gad", "Dani", "Dana", "Tal"]
name = input("Enter your name: ")
found = False
for i in names:
    if name == i:
        found = True
        print("Found")
        names.remove(name)
if found is False:
    print("Not Found")
print(names)


#25
numbers = [10, 50, 5, 99, 20, 40, 70, 90, 35, 84]
evens = [n for n in numbers if n % 2 == 0]
odds = [n for n in numbers if n % 2 == 1]
big20 = [n for n in numbers if n > 20]


# 26
n = [10, 50, 5, 99, 20, 40, 70, 90, 35, 84]
num = int(input("Enter a number: "))
count = 0
for i in n:
    if num == i:
        count += 1
if count == 0:
    print("Not Found")
else:
    print(count)


#27
n1 = [10, 50, 5, 99, 20, 40, 70, 90, 35, 84]
n2 = [12, 7, 25, 30, 9, 44, 18, 3]
new_n = n1 + n2
print(new_n)
print(new_n[0:5])
print(new_n[-5:])
print(new_n[::-1])


#28
n = [10, 50, 5, 99, 20, 40, 70, 90, 35, 84]
num = int(input("Enter a number: "))
flag = False
for i in n:
    if i == num:
        flag = True
if flag is False:
    n.append(num)
print(n)







grades = [85, 72, 90, 55, 100, 63, 48, 77]
choose = 1
while choose != 0:
    choose = int(input("""
===== Grades Management =====

1. Show all grades
2. Add a grade
3. Search for a grade
4. Remove a grade
5. Show passing grades
6. Show failing grades
7. Show highest and lowest grade
8. Show average grade
9. Show first 3 grades
10. Show grades in reverse
0. Exit
"""))

    if choose == 1:
        for i in grades:
            print(i)
    if choose == 2:
        grades.append(input("Enter a grade: "))
    if choose == 3:
        grade = int(input("Enter a grade: "))
        for i in range(len(grades)):
            if grade == grades[i]:
                print(i)
    if choose == 4:
        grades.remove(input("Enter grade to remove: "))
    if choose == 5:
        print([g for g in grades if g > 60])
    if choose == 6:
        print([g for g in grades if g < 60])
    if choose == 7:
        mi = grades[0]
        ma = grades[0]
        for g in grades:
            if g < mi:
                mi = g
            elif g > ma:
                ma = g
        print(f"The maximun is {ma} and minimum is {mi}")
    if choose == 8:
        count = 0
        for g in grades:
            count += g
        if count != 0:
            print(count/ len(grades))
        else:
            continue
    if choose == 9:
        print(grades[:3])
    if choose == 10:
        print(grades[::-1])
    if choose == 11:
        break