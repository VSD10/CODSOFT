import random as r
import string as s
def passgen(l):
    su=s.ascii_uppercase
    sl=s.ascii_lowercase
    sd=s.digits
    sc=s.punctuation
    al=su+sl+sd+sc
    pas=''
    for x in range(l):
        pas+=r.choice(al)
    return pas
print("\t\t\t\t\t\tPASSWORD GENERATOR")
a=True
while a:
    l=int(input("\nENTER A LENGTH OF THE PASSWORD:"))
    n=passgen(l)
    print("\n\nGENERATED PASSWORD IS: ",n)
    print("\n\nWould you like to regenerate?")
    e=int(input("1.Yes\n2.No"))
    if e==2:
        a=False
    elif e==1:
        a=True
    else:
        print("ENTER A CORRECT OPTION")