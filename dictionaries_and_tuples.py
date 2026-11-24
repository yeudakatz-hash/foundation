
#1
numbers = (10, 20, 30, 40, 50)
print(numbers)
print(numbers[0], numbers[-1])
print(len(numbers))
print(numbers[2])


#2
names = ("Dan", "Tal", "Ran", "Shir", "Avi")
for name in names:
    print(name)
print("Shir" in names)
print(len(names))


#3
numbers = (10, 20, 30, 40, 50)
print(numbers[:3])
print(numbers[-3:])
print(numbers[::-1])


#4
product = ("Apple", 3, 100 , "fruits")
for i in range(len(product)):
    print(product[i])


#5
numbers = (10, 20, 30, 40, 50)
count = 0
evens = 0
ma = numbers[0]
for n in numbers:
    count += n
    if n % 2 == 0:
        evens += 1
    if n > ma:
        ma = n
print(f"sun of numbers {count}, even numbers {evens}, maximum number {ma}")


#6
products = ("Laptop", "Mouse", "Keyboard", "Screen", "Printer")
new_product1 = products[0:3]
new_product2 = products[-2:]
new_product3 = new_product1 + new_product2
print(new_product3)


#7
student = {"name": "David",    "age": 22,    "grade": 95}
for k in student.values():
    print(k)


#8
car = {"brand": "Toyota", "model": "corola", "year": 2020, "price": 58000}
car["price"] = 55000
car["year"] = 2022
car["color"] = "red"
print(car)


9
salaries = {    "David": 12000,    "Moshe": 15000,    "Dana": 13500}
c=0
for s in salaries.values():
    print(s)
salaries["David"] = 13000
salaries["Dani"] = 11111
print(salaries)


#10
fruits = {"batata": 10 , "banana": 5 , "apple": 8 , "watermellon": 20}
fruit = input("enter a fruit: ")
if fruit in fruits:
    print(fruits[fruit])
else:
    print("not found")


#11
grades = {"Avi": 95 , "Dina": 91 , "Shir": 75 , "Dana": 100 , "Tal": 62}
for grade in grades:
    print(f"Student: {grade} | Grade: {grades[grade]}")


#12
grades = {    "David": 90,    "Moshe": 75,    "Dana": 100,    "Noa": 55,    "Avi": 82}
avg = 0
maximum = 0
fail = 0
for grade in grades:
    if grades[grade] > maximum:
        maximum = grades[grade]
    avg += grades[grade]
    if grades[grade] > 80:
        print(f"Student: {grade} | Grade: {grades[grade]}")
    elif grades[grade] < 60:
        fail += 1


#13
fruits = {"batata": 10 , "banana": 5 , "apple": 8 , "watermellon": 20}
fruit = input("Enter name of fruit: ")
# if fruit in fruits:
fruits[fruit] = input("Enter a price: ")
print(fruits)


#14
students = [    {"name": "David", "age": 20, "grade": 90},
                {"name": "Moshe", "age": 22, "grade": 75},
                {"name": "Dana", "age": 21, "grade": 100},
                {"name": "Noa", "age": 19, "grade": 55},
                {"name": "Avi", "age": 23, "grade": 82}]

for d in students:
    print(d["name"])
for d in students:
    print(d["grade"])
for d in students:
    if d["grade"] > 80:
        print(d["name"])
count = 0
for d in students:
    count += d["grade"]
print(f"average is {count / len(students)}")


#15
students.append({"name": "Tal", "age": 22, "grade": 72})
students[1]["grade"] = 100
name = input("Enter a name to delete: ")
for s in students:
    if s["name"] == name:
        del s
print(students)


#16
classroom = {"Class A": ["David", "Moshe", "Dana"],
             "Class B": ["Noa", "Avi", "Michael"],
             "Class C": ["Daniel", "Shir", "Yossi"]}
for clas in classroom:
    print(clas)
print(classroom["Class A"])
classroom["Class B"].append("Shay")
classroom["Class C"].remove("Shir")
for clas in classroom:
    print(len(classroom[clas]))


#17
products = {"Laptop": {"price": 4500, "stock": 10},
            "Mouse": {"price": 80, "stock": 50},
            "Keyboard": {"price": 150, "stock": 20}
            }
for product in products:
    print(product , products[product]["price"])
for product in products:
    print(product , products[product]["stock"])
products["Laptop"]["stock"] = 20
products["consula"] = {"price": 1000 , "stock": 22}
print(products)
for product in products:
    if products[product]["price"] > 100:
#         print(product)


#18
employees = [("David", "Development", 15000),
             ("Moshe", "Marketing", 12000),
             ("Dana", "Development", 18000),
             ("Noa", "HR", 11000)
             ]
for employee in employees:
    print(employee[0])
for employee in employees:
    if employee[1] == "Development": print(employee[0])
max_salary = 0
name_max_salary = None
count = 0
for employee in employees:
    count += employee[2]
    if employee[2] > max_salary:
        max_salary = employee[2]
        name_max_salary = employee[0]
print(name_max_salary)
print(f"The avg is {count/ len(employees)}")


#19
inventory = {    "Laptop": 10,    "Mouse": 50,    "Keyboard": 20}
name = input("Enter a product name: ")
if name in inventory:
    quantity = int(input("Enter a quantity of products: "))
    if inventory[name] >= quantity:
        inventory[name] -= quantity
        print(inventory)
    else:
        print("Not enogh products")
else:
    print("The product not found!")


#20
votes = {    "David": 0,    "Moshe": 0,    "Dana": 0}
choose = 0
while choose != 2:
    choose = int(input("""
    1. vote
    2. exit
    """))
    if choose == 1:
        name = input("Enter a name: ")
        if name in votes:
            votes[name] += 1
    if choose == 2:
        print(votes)


#21
contacts = {"yehuda": "0556787540", "loooosh": "0555687502"}
choose = 0
while choose != 6:
    choose = int(input("""
    1. add contacts
    2. search contact
    3. update contact
    4. delete contact
    5. view contacts
    6. exit
    """))
    if choose == 1:
        name = input("Enter a name: ")
        phone = str(input("Enter a number: "))
        contacts[name] = phone
    if choose == 2:
        choose = int(input("""
            1. by name
            2. by number
            """))
        if choose == 1:
            name = input("Enter a name: ")
            print(contacts[name])
        elif choose == 2:
            phone = str(input("Enter a number: "))
            for key in contacts:
                if contacts.get(key) == phone:
                    print(key)
    if choose == 3:
        name = input("Enter a name: ")
        if name in contacts:
            phone = str(input("Enter a number: "))
            contacts[name] = phone
        else:
            print("not found \n you can add contact in press 1")
    if choose == 4:
        contacts.pop(input("Enter a name: "))
    if choose == 5:
        print(contacts)
    if choose == 6:
        print("Bye")

#22
products = [    {"name": "Laptop", "price": 4500, "stock": 10},
                {"name": "Mouse", "price": 80, "stock": 50},
                {"name": "Keyboard", "price": 150, "stock": 20},
                {"name": "Screen", "price": 900, "stock": 15}
                ]
choose = 1
while choose != 0:
    choose = int(input("""
===== Store Management =====

1. Show all products
2. Add product
3. Search product
4. Update product price
5. Update product stock
6. Sell product
7. Show products by price
8. Show products with low stock
9. Show total inventory value
0. Exit

    """))
    if choose == 1:
        print(products)
    elif choose == 2:
        product_name = input("Enter product name: ")
        price = float(input("Enter product price: "))
        quantity = int(input("Enter product quantity: "))
        products.append({"name": product_name, "price": price, "stock": quantity})
    elif choose == 3:
        product_name = input("Enter product name: ")
        for product in products:
            if product["name"] == product_name:
                print(product)
    if choose == 4:
        product_name = input("Enter product name: ")
        for product in products:
            if product["name"] == product_name:
                new_price = int(input("Enter product price: "))
                product["price"] = new_price
    elif choose == 5:
        product_name = input("Enter product name: ")
        for product in products:
            if product["name"] == product_name:
                new_stock = int(input("Enter product price: "))
                product["price"] = new_stock
    elif choose == 6:
        product_name = input("Enter product name: ")
        for product in products:
            if product["name"] == product_name:
                quantity = int(input("Enter num of quantity you want to buy: "))
                if product["stock"] > quantity:
                    product["stock"] -= quantity
                else:
                    print("not enogh quantities")
    elif choose == 7:
        price_to_sort = float(input("Enter price: "))
        for product in products:
            if product["price"] > price_to_sort:
                print(product)
    elif choose == 8:
        quantity_to_sort = int(input("Enter quantities: "))
        for product in products:
            if product["stock"] < quantity_to_sort:
                print(product)
    elif choose == 9:
        total = 0
        for product in products:
            total += product["stock"] * product["price"]
        print(total)
    elif choose == 0:
        print("bye")