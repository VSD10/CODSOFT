class todo():
 
    def __init__(self): 
        self.task=[]

    def view(self):
        print('\t\t\t\t\tHERE ARE THE LIST OF TASKS TO BE DONE')
        for x in range(0,len(self.task)):
            print(x+1,"-",self.task[x])
        print("\nwould you like to continue:\n1.yes \n2.no")
        e = int(input("Your Choice: "))
        if e == 1:
            return True
        else:
            return False
    

    def add(self):
        print('add')
        print("would you like to continue:\n1.yes \n2.no")
        e = int(input("Your Choice: "))
        if e == 1:
            return True
        else:
            return False
    
    def update(self):
        print('UPDATE YOUR TASKS')
        print("1.ADD\n2.MODIFY\n3.DELETE")
        i=int(input("YOUR CHOICE:"))
        if i==1:
            a=input("ENTER A NEW TASK:")
            self.task.append(a)
            print("THE TASK ADDED SUCCESSFULLY!!")
        elif i==2:
            
            print('\t\t\t\t\tHERE ARE THE LIST OF TASKS')
            for x in range(0,len(self.task)):
                print(x+1,"-",self.task[x])
            print("\nENTER THE NO. TO MODIFY")
            mo=int(input("Your Choice:"))
            inn=input("\nENTER A MODIFED TASK::")
            self.task.remove(self.task[mo-1])
            self.task.insert(mo-1,inn)
            print("THE TASK MODIFIED SUCCESSFULLY!!")
        elif i==3:
            print('\t\t\t\t\tHERE ARE THE LIST OF TASKS')
            for x in range(0,len(self.task)):
                print(x+1,"-",self.task[x])
            print("\nENTER THE NO. TO Remove:")
            mo=int(input("Your Choice:"))
            self.task.remove(self.task[mo-1]) 
            print("The task Removed successfully!!")
            
        print("\n\n\nwould you like to continue:\n1.yes \n2.no")
        e = int(input("Your Choice: "))
        if e == 1:
            return True
        else:
            return False

a = True
to = todo()
while a:
 
    print("\t\t\t\t\t\tTO-DO LIST")
    print("1.TO VIEW YOUR LISTS")
    print("2.TO TRACK YOUR PROGRESS")
    print("3.TO UPDATE THE TASKS , ADD OR DELETE")
    print("4.EXIT")
    n = int(input("Your Choice: "))

    if n == 1:
        a = to.view()
    elif n == 2:
        a = to.add()
    elif n == 3:
        a = to.update()
    elif n == 4:
        break
    else:
        print("\n\n\nENTER A CORRECT CHOICE")
        print("would you like to continue:\n1.yes \n2.no")
        e = int(input("Your Choice: "))
        if e == 1:
            continue
        else:
            break
