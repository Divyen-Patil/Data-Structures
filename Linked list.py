###   A python program to create a linked list and perform operation on the list

l1 = []

l1.append("India")
l1.append("America")
l1.append("England")

print("The existing list is : ", l1)

choice = 0
while choice<5:
    print("1. Add elements")
    print("2. Remove elements")
    print("3. Replace elements")
    print("4. Search for elements")
    print("5. Exit")

    choice = int(input("Enter the choice : "))

    if choice==1:
        element = input("Enter element : ")
        pos = int(input("Enter the position"))
        l1.insert(pos, element)

    elif choice==2:
        try:
            element = input("Enter the element : ")
            l1.remove(element)
        except ValueError:
            print("Element not found!")

    elif choice==3:
        element = input("Enter element : ")
        pos = int(input("Enter the position"))
        l1.pop(pos)
        l1.insert(pos, element)

    elif choice==4:
        element = input("Enter the element to be searched : ")
        try:
            pos = l1.index(element)
            print("The position of the element is :", pos)

        except ValueError:
            print("Element not found")

    else:
        break

    print("List = ", l1)



