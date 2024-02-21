from vpython import *
from sys import exit

def menu():
    print('1. Curve')
    print('2. Sphere')
    print('3. Cone')
    print('4. Arrow')
    print('5. Rings')
    print('6. Cylinder')

ch = "y"
while ch != "n":
    scene = canvas()
    menu()

    choice = int(input('Enter choice: '))
    if choice == 1:
        curve()
    elif choice == 2:
        sphere()
    elif choice == 3:
        cone()
    elif choice == 4:
        arrow()
    elif choice == 5:
        ring()
    elif choice == 6:
        cylinder()
    else:
        print('Invalid choice')

    ch = input('Do you want to continue (y/n)? ').lower()
    scene.delete()

exit()
