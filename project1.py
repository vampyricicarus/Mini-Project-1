def menu():
    print("Welcome to the To-Do List App! \n Menu: \n 1. Add a task \n 2. View tasks \n 3. Mark a task as complete \n 4. Delete a task \n 5. Quit")

toDo = ["wash dishes", "vaccuum", "wipe counters"]

menu()

def addTask():
    x = input("Add an item to the to do list= ")
    y = input("Is the item complete or incomplete? ")
    toDo.append(x + "-" + y)
    print(toDo)
    return

def deleteTask():
    try:
        toDo.remove(input("Which task to remove? "))
        print(toDo)
    except ValueError:
        print("Pick another item")
    return

def quitFunction():
    x = input("Would you like to quit? ")
    if x == "yes":
        quit
    else:
        return addTask
    return

def markComplete():
    x = input("Mark as complete? ")
    if x == "yes":
        toDo.append("Complete")

while input("Which menu item would you like? ") == "Add task":
    addTask()
    if input("Quit? ") == "no":
        menu()
        if input("Which menu option to do? ") == "Delete task":
            deleteTask()
            if input("Quit? ") == "no":
                menu()
            else:
                quit
    else:
        quit
            
