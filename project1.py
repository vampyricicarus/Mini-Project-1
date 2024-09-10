print("Welcome to the To-Do List App! \n Menu: \n 1. Add a task \n 2. View tasks \n 3. Mark a task as complete \n 4. Delete a task \n 5. Quit")
toDo = ["wash dishes", "vaccuum", "wipe counters"]

def addTask():
    x = input("Add an item to the to do list= ")
    y = input("Is the item complete or incomplete? ")
    toDo.append(x + "-" + y)
    print(toDo)
    return
addTask()

def deleteTask():
    toDo.remove(input("Which task to remove? "))
    print(toDo)
    return

deleteTask()

def quitFunction():
    x = input("Would you like to quit? ")
    if x == "yes":
        quit
    else:
        return addTask
    return

quitFunction()