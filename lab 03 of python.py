#LAB3

#1
"""
x1 = float(input("Enter x1: "))
y1 = float(input("Enter y1: "))
r = float(input("Enter radius: "))

x2 = float(input("Enter x2: "))
y2 = float(input("Enter y2: "))

distance = (x2 - x1) * (x2 - x1) + (y2 - y1) * (y2 - y1)
radius = r * r

if distance < radius:
    print("Point is inside the circle")
elif distance == radius:
    print("Point is on the boundary of the circle")
else:
    print("Point is outside the circle")
"""
#2
"""
s = float(input("Enter the side of the pentagon: "))
area = (5 * s * s) / (4 * 0.726)
print("Area of pentagon =", area)
"""
#3
"""
a = float(input("Enter first angle: "))
b = float(input("Enter second angle: "))
c = float(input("Enter third angle: "))

if a <= 0 or b <= 0 or c <= 0:
    print("Invalid triangle")
elif a + b + c != 180:
    print("Invalid triangle")
elif a == 90 or b == 90 or c == 90:
    print("Right-angled triangle")
elif a > 90 or b > 90 or c > 90:
    print("Obtuse-angled triangle")
else:
    print("Acute-angled triangle")
"""
#4
"""
number = int(input("Enter a 4 digit number: "))

first = number // 1000
second = (number // 100) % 10
third = (number // 10) % 10
fourth = number % 10

first_sum = first + second
last_sum = third + fourth

print("Sum of first two digits =", first_sum)
print("Sum of last two digits =", last_sum)

if first_sum == last_sum:
    print("The two sums are equal")
else:
    print("The two sums are not equal")
"""
#5
"""
number = int(input("Enter a 5 digit number: "))

d1 = number // 10000
d2 = (number // 1000) % 10
d3 = (number // 100) % 10
d4 = (number // 10) % 10
d5 = number % 10

largest = d1
position = 1

if d2 > largest:
    largest = d2
    position = 2

if d3 > largest:
    largest = d3
    position = 3

if d4 > largest:
    largest = d4
    position = 4

if d5 > largest:
    largest = d5
    position = 5

print("Largest digit =", largest)
print("Position =", position)
"""
#6
"""
a = int(input("Enter a: "))
b = int(input("Enter b: "))
c = int(input("Enter c: "))

a = a + b + c
b = a - b - c
c = a - b - c
a = a - b - c

print("a =", a)
print("b =", b)
print("c =", c)
"""
#7
"""
number = int(input("Enter a 3 digit number: "))

if number < 100 or number > 999:
    print("Invalid input")
else:
    first = number // 100
    second = (number // 10) % 10
    third = number % 10

    sum_digits = first + second + third

    if number % sum_digits == 0:
        print("Harshad number")
    else:
        print("Not a Harshad number")
"""
#8
"""
water = float(input("Enter initial quantity of water: "))
days = int(input("Enter number of days: "))

if water < 0 or days < 0:
    print("Invalid input")
else:
    water = water * (0.95 ** days)
    added_water = 10 * (1 - (0.95 ** days)) / 0.05
    water = water + added_water

    print("Amount of water after", days, "days =", water)
"""
#9
"""
a1 = float(input("Enter a1: "))
b1 = float(input("Enter b1: "))
c1 = float(input("Enter c1: "))

a2 = float(input("Enter a2: "))
b2 = float(input("Enter b2: "))
c2 = float(input("Enter c2: "))

D = a1 * b2 - a2 * b1
Dx = c1 * b2 - c2 * b1
Dy = a1 * c2 - a2 * c1

if a1 == 0 and b1 == 0:
    print("Invalid first line")
elif a2 == 0 and b2 == 0:
    print("Invalid second line")
elif D != 0:
    x = Dx / D
    y = Dy / D

    print("x =", x)
    print("y =", y)

elif Dx == 0 and Dy == 0:
    print("The lines are coincident")
else:
    print("The lines are parallel")
"""




