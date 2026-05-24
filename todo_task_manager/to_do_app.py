# TO DO AAPLICATION 

task_list = []
while True:
    print("== MENU BAR ==")
    print("1. Add Task")
    print("2. View Task")
    print("3. Remove Task")
    print("4. Exit")

    select = input("ENTER YOUR CHOICE :")

    if select == '1':
        task = input('Enter your task here :')
        task_list.append(task)
    
    elif select == '2':
        print(task_list)

    elif select == '3':
        task = input('Enter your task here :')
        if task in task_list:
            task_list.remove(task)
            print(task_list)
        else:
            print("task not found ")
    
    elif select == '4':
        print('You Are Out From This ..')
        break

    else:
        print("invalid select.")