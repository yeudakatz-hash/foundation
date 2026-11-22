
#1
num1 = 25
num2 = 7

print(f"""
Arithmetic operations on numbers {num1}, {num2}
Addition {num1 + num2}
Subtraction {num1 - num2}
Multiplication {num1 * num2}
Division {num1 / num2}
Integer division {num1 // num2}
Remainder {num1 % num2}
Exponentiation {num1 ** num2}
""")


#2
balance = 1000
print(f"""
balance {balance}
add 250: {balance + 250}
sub 100: {balance - 100}
mul2: {balance * 2}
div4: {balance / 4}
""")


#3
price = int(input("Enter price: "))
discount = int(input("Enter discount percent: "))
print(f"the discount is {(price * discount) / 100} and new price is {price - ((price * discount) / 100)}")


#4
money = int(input("Enter value of money: "))
percent = int(input("Enter percent of ribiss per 1 year: "))
print(f"the ribisss is {(money * percent) / 100} and new value you need to pay is {money + ((money * percent) / 100)}")



#5
grade1 = float(input("Enter grade 1: "))
grade2 = float(input("Enter grade 2: "))
grade3 = float(input("Enter grade 3: "))
print(f"the avg of the grades is {grade1 + grade2 + grade3 / 3 }")


#6
first_name = "David"
last_name = "Cohen"
city = "Tel Aviv"
print(f"Hello, my name is {first_name} {last_name} and I live in {city}.")
print("Hello, my name is" , first_name , last_name , "and I live in" , city, ".")


#7
name = input("Enter your name: ")
print(f"""
{name}
The length of the word {len(name)}
the name in upper: {name.upper()}
the name in lower: {name.lower()}
""")


#8
list = input("Enter a list:")
print(f"""
All letters are uppercase: {list.upper()}
All letters are lowercase: {list.lower()}
Capitalize the first letter: {list.capitalize()}
Every word begins with a capital letter: {list.title()}
""")



#9
name = input("Enter your name: ")
print(f"""
original text: {name}
text after removing whitespace: {name.strip()}
length of the text before the removal: {len(name)}
length of the text after the removal: {len(name.strip())}
""")



#10
sentence = "I love Java programming"
print(f"""
change word: {sentence.replace("Java", "Python")}
count word:{sentence.count("love")}
start with:{sentence.startswith("I")}
end with: {sentence.endswith("programing")}
""")



#11
word = "Programming"
print(f"""
first char in word: {word[0]}
last char in word: {word[-1]}
3rd char: {word[2]}
3 first chars: {word[0:3]}
last 4 chars: {word[-4:]}
reversed word {word[::-1]}
""")


#12
a = "100"
b = "25"
c = 10
d = 5.5

a = int(a)
b = float(b)
c = str(c)
d = int(d)
print(a , type(a))
print(b , type(b))
print(c , type(c))
print(d , type(d))



#13
age = input("Enter your age: ")
age = int(age)
print(age + 10)
#בגלל שאי אפשר לחבר משתנה מסוג int עם str לכן צריך להמיר בהתחלה את הטיפוס


#14
price = float(input("Enter price without VAT: "))
print(f"the total price with VAT is {price * 1.18}")


#15
first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
age = input("Enter your age: ")
monthly_salary = int(input("enter salary per month: "))
senior = int(input("Enter a years of seniority"))
print(f"""
=====WORKER CARD=====
name: {first_name} {last_name}
age: {age}
senior: {senior}
The annual salary: {monthly_salary * 12}
The salary after a 5% increase: { 1.05 * (monthly_salary * 12)}
The number of characters in the full name: {len(first_name) + len(last_name)}
""")



#16
usd_rate = 3.25
shekel = float(input("enter num of shekels: "))
print(f"you have {shekel/usd_rate} in usd")
print(print(f"you have {shekel/3.75} in euro"))
print(f"you have {0.98 * (shekel/ 3.25)} in usd or {0.98 * (shekel/ 3.75)} in euro after commition ")


#17
first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
year_of_birth = input("Enter your year of birth: ")
print(f"your new email address is: {first_name.lower()}.{last_name.lower()}.{year_of_birth}@gmail.com")


#18
list = input("enter a list: ")
print(f"""
The original sentence: {list}
The number of characters in the sentence: {len(list)}
The sentence in uppercase: {list.upper()}
The sentence in lowercase: {list.lower()}
The sentence in reverse order: {list[::-1]}
The number of times the letter 'a' appears in the sentence: {list.count("a")}
The sentence after replacing spaces with hyphens: {list.replace(" ", "-")}
""")


#19
name = input("enter name")
product_name = input("Enter product name:")
product_price = float(input("enter price to product: "))
quantity = int(input("enter num of quantity: "))
discount = int(input("enter num of percent of discount: "))
vat = int(input("Enter a percent of vat: "))
print(f"""
================================
          PURCHASE INVOICE
================================

Customer: {name}
Product: {product_name}

Unit Price: {product_price}
Quantity: {quantity}

Subtotal: {product_price * quantity}
Discount: {discount}
After Discount: {(product_price * quantity) * ((100 - discount)/ 100)}

VAT: {vat}%
VAT Amount: {(vat / 100) * (product_price * quantity) * ((100 - discount)/ 100)}

TOTAL: {(1 + (vat/ 100)) * (product_price * quantity) * ((100 - discount)/ 100)}

================================
       THANK YOU FOR SHOPPING
================================

""")