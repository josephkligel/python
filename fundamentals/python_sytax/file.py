# variable decleration
num1 = 42
# Number primitive type
num2 = 2.3
# Boolean primitive type
boolean = True
# String primitive type
string = 'Hello World'
# list initialize
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives']
# dictionary initialize
person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False}
# tuple initialize
fruit = ('blueberry', 'strawberry', 'banana')
# type check
print(type(fruit))
# List access value
print(pizza_toppings[1])
# List add value
pizza_toppings.append('Mushrooms')
# Dictionary access value
print(person['name'])
# Dictionary change value
person['name'] = 'George'
# Dictionary add value
person['eye_color'] = 'blue'
# Tuple access value
print(fruit[2])

if num1 > 45:
    print("It's greater")
else:
    print("It's lower")
# length check
if len(string) < 5:
    print("It's a short word!")
elif len(string) > 15:
    print("It's a long word!")
else:
    print("Just right!")

for x in range(5):
    print(x)
for x in range(2,5):
    print(x)
for x in range(2,10,3):
    print(x)
x = 0
while(x < 5):
    print(x)
    x += 1

pizza_toppings.pop()
pizza_toppings.pop(1)

print(person)
person.pop('eye_color')
print(person)

for topping in pizza_toppings:
    if topping == 'Pepperoni':
        continue
    print('After 1st if statement')
    if topping == 'Olives':
        break

def print_hello_ten_times():
    for num in range(10):
        print('Hello')

print_hello_ten_times()

def print_hello_x_times(x):
    for num in range(x):
        print('Hello')

print_hello_x_times(4)

def print_hello_x_or_ten_times(x = 10):
    for num in range(x):
        print('Hello')

print_hello_x_or_ten_times()
print_hello_x_or_ten_times(4)

# comment - single line
"""
Bonus section
"""

# comment - multiline
# print(num3)
# num3 = 72
# fruit[0] = 'cranberry'
# print(person['favorite_team'])
# print(pizza_toppings[7])
#   print(boolean)
# fruit.append('raspberry')
# fruit.pop(1)