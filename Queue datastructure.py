### A Python program to perform some operation on a queue

from queue import Queue

q = Queue()

choice = 0
while choice<4:
    print("Queue Operations")
    print("1. Add element")
    print("2. Delete element")
    print("3. Search for element")
    print("4. Exit")

    choice = int(input("Enter tour Choice : "))

    if choice == 1:
        element = int(input("Enter the element : "))
        q.add(element)

    elif choice == 2:
        element = q.delete()
        if element == -1:
            print("The queue is empty")

        else:
            print("The removed element : ", element)

    elif choice == 3:
        element = int(input("Enter the element to be searched : "))
        pos = q.search(element)

        if pos == -1:
            print("The queue is empty")

        elif pos == -2:
            print("Element not found in the queue")

        else:
            print("Element is found at position : ", pos)

    
    else:
        break

    print("Queue = ", q.display)
    