def triangle_type(a, b, c):
    if a + b > c and a + c > b and b + c > a:
        if a == b == c:
            return "Equilateral"
        elif a == b or b == c or a == c:
            return "Isosceles"
        else:
            return "Scalene"
    else:
        return "Not a triangle"

def acute_triangle_check(a, b, c):
    if a + b > c and a + c > b and b + c > a:
        sides = [a, b, c]
        sides.sort()
        if sides[0]**2 + sides[1]**2 > sides[2]**2:
            return "Acute"
        elif sides[0]**2 + sides[1]**2 == sides[2]**2:
            return "Right"
        else:
            return "Obtuse"
    return "Not a triangle"

print("Triangle Type Checker")
print("=====================")
a = float(input("Enter first side: "))
b = float(input("Enter second side: "))
c = float(input("Enter third side: "))

type_result = triangle_type(a, b, c)
angle_result = acute_triangle_check(a, b, c)

print("Triangle Type: " + type_result)
print("Triangle Angle Type: " + angle_result)