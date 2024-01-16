class todo():
     def __init__(self): 
        self.task=[]
        self.status=[]
     def view(self):
        print('\t\t\t\t\tHERE ARE THE LIST OF TASKS TO BE DONE')
        i=1
        for x,y in zip(self.task,self.status):
            print(i,".",x,'-',y)
            i+=1
        i=1
        print("\nwould you like to continue:\n1.yes \n2.no")
        e = int(input("Your Choice: "))
        if e == 1:
            return True
        else:
            return False
     def add(self):
        print('\t\t\t\t HERE WHERE YOU CAN TRACK YOUR PROGRESS!!!!')

        print("1.MARK AS COMPLETE\n2.MARK AS NOT COMPLETED")
        aa=int(input("Your choice:"))
        if aa==1:
            print('\t\tHERE ARE THE LIST OF YOUR TASKS')
            i=1
            for x,y in zip(self.task,self.status):
                print(i,".",x,'-',y)
                i+=1
            i=1
            c=''
            s=int(input("Select the task:"))
        print("would you like to continue:\n1.yes \n2.no")
        e = int(input("Your Choice: "))
        if e == 1:
            return True
        else:
            return False
     def update(self):
        print('UPDATE YOUR TASKS')
        print("1.ADD\n2.MODIFY\n3.UPDATE STATUS\n4.DELETE")
        i=int(input("YOUR CHOICE:"))
        if i==1:
            a=input("ENTER A NEW TASK:")
            self.task.append(a)
            self.status.append("NOT COMPLETED")
            print("THE TASK ADDED SUCCESSFULLY!!")
        elif i==2:
            
            print('\t\t\t\t\tHERE ARE THE LIST OF TASKS')
            i=1
            for x,y in zip(self.task,self.status):
                print(i,".",x,'-',y)
                i+=1
            i=1
            print("\nENTER THE NO. TO MODIFY")
            mo=int(input("Your Choice:"))
            inn=input("\nENTER A MODIFED TASK::")
            self.task.remove(self.task[mo-1])
            self.task.insert(mo-1,inn)
            if self.status[mo-1]=='COMPLETED':
                self.status.remove(self.status[mo-1])
                self.status.insert(mo-1,'NOT COMPLETED')
                
            print("THE TASK MODIFIED SUCCESSFULLY!!")
        elif i==3:
            print("\t\t\t HERE YOU CAN UPDATE THE STATUS OF THE TASKS")
            i=1
            print('\t\t\t\t\tHERE ARE THE LIST OF TASKS')
            for x,y in zip(self.task,self.status):
                print(i,".",x,'-',y)
                i+=1
            print("Select the Task to Update the task")
            s=int(input("Your Choice:"))
            self.status.remove(self.status[s-1])
            self.status.insert(s-1,'COMPLETED')
        
        elif i==4:
            print('\t\t\t\t\tHERE ARE THE LIST OF TASKS')
            i=1
            for x,y in zip(self.task,self.status):
                print(i,".",x,'-',y)
                i+=1
            i=1
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
    print("\t\t\t\t\t\tDM-TO-DO LIST")
    print("1.TO VIEW YOUR LISTS")
    print("2.TO TRACK YOUR PROGRESS")
    print("3.TO UPDATE YOUR TASK")
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
print("\n\n\nTHANKS FOR USING OUR USING DM-TO-DO LISTS")
