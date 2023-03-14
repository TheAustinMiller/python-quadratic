# QuadraticEquation.py

"""
Author: Austin Miller
Class: CS 170/01
Purpose: Complete the quadratic equation using the given inputs
"""
import math

a, b, c = 0, 0, 0


def main():
    a = eval(input("Enter the 'a' value: "))
    b = eval(input("Enter the 'b' value: "))
    c = eval(input("Enter the 'c' value: "))
    discriminant = b ** 2 - 4 * a * c

    while discriminant < 0:
        print("This equation has no real roots.")

        a = float(input("Enter a: "))
        b = float(input("Enter b: "))
        c = float(input("Enter c: "))

        discriminant = b ** 2 - 4 * a * c

    if discriminant > 0:
        firstRoot = (-b + math.sqrt(discriminant)) / (2 * a)
        secondRoot = (-b - math.sqrt(discriminant)) / (2 * a)

        print("This equation has two roots:", format(firstRoot, "0.3f"), "and", format(secondRoot, "0.3f"))
    elif discriminant == 0:
        root = -b / (2 * a)

        print("This equation has one real root:", format(root, "0.3f"))


main()
