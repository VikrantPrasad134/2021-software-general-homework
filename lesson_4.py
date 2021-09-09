#Assignment 1
import math
def conversion(fahrenheit):
    celcius = (fahrenheit - 32) * 5/9
    print(str(fahrenheit) + "℉ can be converted to " + str(celcius) + "℃.")

def sphere_volume(radius):
    volume = 4/3 * math.pi * (radius * radius * radius)
    print("The volume of a sphere with a radius of " + str(radius) + " is " + str(volume) + ".")

def factorial(num):
    if num < 0:
        return None
    factorial = 1
    for i in range(1,num + 1):
        factorial = factorial * i
    print(str(factorial))




conversion(78)
sphere_volume(57)
factorial(5)
