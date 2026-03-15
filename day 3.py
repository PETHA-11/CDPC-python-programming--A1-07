# 1. Take user's name and age as input and print message
name = input("Enter your name: ")
age = int(input("Enter your age: "))
print("Hello", name, ", you are", age, "years old.")

# 2. Calculate perimeter of a rectangle
length = int(input("Enter length: "))
width = int(input("Enter width: "))
print("Perimeter =", 2*(length+width))

# 3. Convert kilometers into meters and centimeters
km = float(input("Enter kilometers: "))
print("Meters =", km*1000)
print("Centimeters =", km*100000)

# 4. Calculate total bill amount for 3 products
p1 = float(input("Enter price of product 1: "))
p2 = float(input("Enter price of product 2: "))
p3 = float(input("Enter price of product 3: "))
print("Total bill =", p1+p2+p3)

# 5. Convert hours into minutes and seconds
hours = int(input("Enter hours: "))
print("Minutes =", hours*60)
print("Seconds =", hours*3600)

# 6. Calculate area of a triangle
base = float(input("Enter base: "))
height = float(input("Enter height: "))
print("Area =", (base*height)/2)

# 7. Take a number and print its double and triple
n = int(input("Enter number: "))
print("Double =", n*2)
print("Triple =", n*3)

# 8. Calculate total number of seconds in given days
days = int(input("Enter days: "))
print("Seconds =", days*24*60*60)

# 9. Convert rupees into paise
rupees = int(input("Enter rupees: "))
print("Paise =", rupees*100)

# 10. Calculate total number of students in a class
boys = int(input("Enter number of boys: "))
girls = int(input("Enter number of girls: "))
print("Total students =", boys+girls)
