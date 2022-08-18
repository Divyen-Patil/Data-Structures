###  A python program to create and use deque

from collections import deque

d = deque()

choice = 0
while choice<7:
    print("Deque operations")
    print("1. Add elements at front")
    print("2. Remove elements at front")
    print("3. Add elements at rear")
    print("4. Remove elements at rear")
    print("5. Remove elements in the middle")
    print("6. Search for elements")
    print("7. Exit")

    choice = int(input("Enter your choice : "))

    if choice == 1:
        element = input("Enter the element : ")
        d.appendleft(element)

    elif choice == 2:
        if len(d) == 0:
            print("The deque is empty")

        else:
            d.popleft()


    elif choice == 3:
        element = input("Enter the element : ")
        d.append(element)

    elif choice == 4:
        if len(d) == 0:
            print("The deque is empty")

        else:
            d.pop()


    elif choice == 5:
        element = input("Enter the element : ")
        try:
            d.remove(element)

        except ValueError:
            print("Element not found")

    elif choice == 6:
        element = input("Enter the element to be searched : ")
        c = d.count(element)
        print("No. of times ehe element found : ", c)

    else:
        break

    print("Deque : ", end = "")
    for i in d:
        print(i, " ", end="")
    print()