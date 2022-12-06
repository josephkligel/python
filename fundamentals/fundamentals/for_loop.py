# Basics
print("-" * 10)

for i in range(0, 151):
    print(i)

# Multiples of five
print("-" * 10)

for i in range(5, 1001):
    if(i % 5 == 0):
        print(i)

# Counting the dojo way
print("-" * 10)

for i in range(1, 101):
    if(i % 10 == 0):
        print("Coding Dojo")
    elif(i % 5 == 0):
        print("Coding")
    else:
        print(i)

# Whoa. That sucker is huge
print("-" * 10)

sum = 0
for i in range(0, 500001):
    if(i % 2 != 0):
        sum += i

print("Total sum is", sum)

# Countdown by fours
print("-" * 10)

for i in range(2018, 0, -4):
    print(i)

# Flexible counter
print("-" * 10)

lowNum = 2
highNum = 9
mult = 3

for i in range(lowNum, highNum+1):
    if(i % mult == 0):
        print(i)