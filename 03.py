#ASSIGMENT_03
def check_right_triangle(a, b, c):
    sides = [a, b, c]
    sides.sort()

    if sides[0] ** 2 + sides[1] ** 2 == sides[2] ** 2:
        print("It is a right-angled triangle.")
    else:
        print("It is not a right-angled triangle.")

a = float(input("Enter first side: "))
b = float(input("Enter second side: "))
c = float(input("Enter third side: "))

check_right_triangle(a, b, c)