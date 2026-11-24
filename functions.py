
#1
def say_hello():
    print("Hello World!")
say_hello()
say_hello()
say_hello()


#2
def show_welcome():
    print("Welcome!!")


#3
def show_meenu():
    print("""
===== Main Menu =====
1. Start
2. Settings
3. Exit
    """)


#4
def show_numbers():
    for i in range(1,11):
        print(i)


#5
def show_even_numbers():
    print([i for i in range(1,101) if i % 2 == 0])


#6
def show_stars():
    print("**********")
def five_times():
    for i in range(5):


#7
def greet(name):
    print(f"Hello {name}")


#8
def show_age(age):
    print(f"you are {age} years old")


#9
def calculate_sum(n1, n2):
    print(n1 +n2)


#10
def calculate_average(n1 ,n2 ,n3):
    print((n1 + n2 + n3)/ 3)


#11
def check_even(n):
    if n % 2 == 0: print("Even")
    else: print("Odd")


#12
def check_password(password):
    if password == "123456": print("Access Granted")
    else: print("Access Denied")


#13
def calculate_discount(price, discount):
    print(((100 - discount) / 100) * price)


#14
def show_range(n1, n2):
    mi = min(n1 , n2)
    ma = max(n1 , n2)
    for i in range(mi, ma + 1):
        print(i)


#15
def print_rectangle(he, we):
    for i in range(he):
        for j in range(we):
            print("*", end="")
        print()


#16
def multiply(n1, n2):
    return n1 * n2


#17
def get_full_name(f_name, l_name):
    return f_name + l_name


#18
def get_max(n1, n2):
    if n1> n2:
        return n1
    return n2


#19
def is_positive(n):
    return True if n >0 else False


#20
def calculate_tax(price, tax):
    return price * (1 + (tax / 100))


#21
def get_grade_status(grade):
    if grade >= 90:
        return "Excellent"
    if 75 >= grade > 90:
        return "Good"
    if 60 >= grade > 75:
        return "Average"
    return "Failed"


#22
def count_digits(n):
    return len(str(n))


#23
def calculate_power(n, power):
    b = n
    for i in range(power - 1):
        n *= b
    return n


#24
def print_list(l):
    print(*l)


#25
def get_list_sum(l):
    count = 0
    for i in l:
        count += i
    return count


#26
def get_list_average(l):
    count = 0
    if len(l) == 0:
        return 0
    for i in l:
        count += i
    return count / len(l)


#27
def find_numbers(l, n):
    for i in l:
        if i == n:
            return True
    return False


#28
def find_max(l):
    m = l[0]
    for i in l:
        if i > m:
            m = i
    return m


#29
def get_even_numbers(l):
    return [e for e in l if e % 2 == 0]


#30
def get_long_names(l):
    return [n for n in l if len(n) > 4]


#31
def reverse_list(l):
    return l[::-1]


#32
def count_occurrences(l , n):
    return l.count(n)


#33
def remove_duplicates(l):
    not_exist = []
    for i in l:
        if i not in not_exist:
            not_exist.append(i)
    return not_exist


#34
def calculate_final_price(price, discount):
    total = price * ((100 - discount) / 100)
    if total > 500:
        return total * 0.95
    return total


#35
def check_list(l):
    evens = 0
    odds = 0
    count = 0
    for i in l:
        if i % 2 == 0:
            evens += 1
        else:
            odds += 1
        count += i
    return f"{evens} evens, {odds} odds, sum numbers: {count}"


#36
def analyze_grades(l):
    ma = 0
    mi = 0
    pas = 0
    count = 0
    for i in l:
        if i < mi: mi = i
        elif i> ma: ma = i
        if i > 60: pas += 1
        count += i
    return f"min grade {mi}, max grade {ma}, passed: {pas} , avg: {count / len(l)}"


#37
def validate_user(password, user_name):
    return True if user_name and len(password) > 6 else False


#38
def search_students(l , n):
    for i in l:
        if i["name"] == n:
            return i
    return None


#39
def calculate_cart_total(l):
    total = 0
    for i in l:
        total += i["price"] * i["quantity"]
    return total


#40
def get_fibonacci(num):
    a = [0,1]
    for i in range(num-2):
        a.append(a[-1] + a[-2])
    return a



#43
n = 10
def increase():
    n= 10
    print(n + 10)
increase()
print(n)


#44
l = []
def appen():
    l.append(10)
    print(l)
appen()
print(l)


#45
def aaa(l):
    a = l[:2]
    a.append(44)
    return a
l = [2,5,4,7]
print(aaa(l))
print(l)






def show_menu():
    choose = int(input("""
    ===== Student Management =====
    
    1. Show all students
    2. Add student
    3. Search student
    4. Update student grade
    5. Remove student
    6. Show passing students
    7. Show students above average
    8. Show highest grade
    0. Exit
        """))
    return choose

def get_name():
    name = input("Enter a name: ")
    return name

def get_grade():
    grade = input("Enter a grade: ")
    return grade

def show_students(students):
    return [student["name"] for student in students]

def add_student(students):
    name = get_name()
    age = get_grade()
    grade = get_grade()
    students.append({"name": name , "age": age, "grade": grade})

def search_student(students):
    name = get_name()
    for student in students:
        if student["name"] == name:
            return student

def update_grade(students):
    name = get_name()
    grade = get_grade()
    for student in students:
        if student["name"] == name:
            student["grade"] = grade

def remove_student(students):
    name = get_name()
    for student in students:
        if student["name"] == name:
            students.remove(student)

def get_passing_students(students):
    return [student["name"] for student in students if student["grade"] > 60]

def get_average(students):
    count = 0
    for student in students:
        count += student["grade"]
    return count / len(students)

def get_highest_grade(students):
    maximum = 0
    for student in students:
        if student["grade"] > maximum:
            maximum = student["grade"]
    return maximum

def show_students_above_average(students):
    return [student["name"] for student in students if student["grade"] > get_average(students)]





def main():
    students = [
    {"name": "David", "age": 20, "grade": 90},
    {"name": "Moshe", "age": 22, "grade": 75},
    {"name": "Dana", "age": 21, "grade": 100},
    {"name": "Noa", "age": 19, "grade": 55},
    {"name": "Avi", "age": 23, "grade": 82}
    ]

    flag = True
    while flag:
        choose = show_menu()

        if choose == 1:
            print(show_students(students))

        if choose == 2:
            add_student(students)

        if choose == 3:
            print(search_student(students))

        if choose == 4:
            update_grade(students)

        if choose == 5:
            remove_student(students)

        if choose == 6:
            print(get_passing_students(students))

        if choose == 7:
            print(show_students_above_average(students))

        if choose == 8:
            print(get_highest_grade(students))

        if choose == 0:
            print("Bye")
            flag = False

main()