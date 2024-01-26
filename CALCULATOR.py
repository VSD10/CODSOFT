#calculator project
import math
class calculator:
    def add(self):
            print("\t\t\t\t\tADDITON OPERATION")
            i1=int(input("ENTER A NUMBER 1:"))
            i2=int(input("ENTER A NUMBER 2:"))
            print("RESULT ADDITION OF TWO VALUES:\t",i1+i2)
            print("\nwould you like to \n1.Continue\n2.Add another value \n3.Exit")
            iii=int(input('Your Choice:'))

            if iii==2:
                 cal.add()
            elif iii==1:
                 return True
            elif iii==3:
                 return False
            else:
                 print("CHOOSE A CORRECT OPTION:")
                 print("\n")
                 print("\nwould you like to \n1.Continue\n2.Add another value \n3.Exit")
                 iii=int(input('Your Choice:'))
                 if iii==2:
                    cal.add()
                 elif iii==1:
                      return True
                 elif iii==3:
                    return False
            
    def sub(self):
            print("\t\t\t\t\tSUBTRACTION OPERATION")
            i1=int(input("ENTER A NUMBER 1:"))
            i2=int(input("ENTER A NUMBER 2:"))
            print("RESULT SUBTRACTION OF TWO VALUES:\t",i1-i2)
            print("\nwould you like to \n1.Continue\n2.Add another value \n3.Exit")
            iii=int(input('Your Choice:'))
            if iii==2:
                 cal.sub()
            elif iii==1:
                 return True
            elif iii==3:
                 return False
            else:
                 print("CHOOSE A CORRECT OPTION:")
                 print("\n")
                 print("\nwould you like to \n1.Continue\n2.Add another value \n3.Exit")
                 iii=int(input('Your Choice:'))
                 if iii==2:
                    cal.add()
                 elif iii==3:
                    return False 
                 elif iii==1:
                    return True           
    def mul(self):
            print("\t\t\t\t\tMULTIPLICATION OPERATION")
            i1=int(input("ENTER A NUMBER 1:"))
            i2=int(input("ENTER A NUMBER 2:"))
            print("RESULT MULTILPLICATION OF TWO VALUES:\t",i1*i2)
            print("\nwould you like to \n1.Continue\n2.Add another value \n3.Exit")
            iii=int(input('Your Choice:'))
            if iii==2:
                 cal.mul()
            elif iii==3:
                 return False
            elif iii==1:
                 return True
            else:
                 print("CHOOSE A CORRECT OPTION:")
                 print("\n")
                 print("\nwould you like to \n1.Continue\n2.Add another value \n3.Exit")
                 iii=int(input('Your Choice:'))
                 if iii==2:
                    cal.add()
                 elif iii==1:
                      return True
                 elif iii==3:
                    return False
    def div(self):
            print("\t\t\t\t\tDIVISION OPERATION")
            i1=int(input("ENTER A NUMBER 1:"))
            i2=int(input("ENTER A NUMBER 2:"))
            print("RESULT DIVISION OF TWO VALUES:\t",i1/i2)
            print("\nwould you like to \n1.Continue\n2.Add another value \n3.Exit")
            iii=int(input('Your Choice:'))
            if iii==2:
                 cal.div()
            elif iii==3:
                 return False 
            elif iii==1:
                 return True           
            else:
                 print("CHOOSE A CORRECT OPTION:")
                 print("\n")
                 print("\nwould you like to \n1.Continue\n2.Add another value \n3.Exit")
                 iii=int(input('Your Choice:'))
                 if iii==2:
                    cal.add()
                 elif iii==1:
                      return True                    
                 elif iii==3:
                    return False   
    def mod(self):
            print("\t\t\t\t\tMODULUS OPERATION")
            i1=int(input("ENTER A NUMBER 1:"))
            i2=int(input("ENTER A NUMBER 2:"))
            print("RESULT MODULUS OF TWO VALUES:\t",i1%i2)
            print("\nwould you like to \n1.Continue\n2.Add another value \n3.Exit")
            iii=int(input('Your Choice:'))
            if iii==2:
                 cal.mod()
            elif iii==1:
                 return True
            elif iii==3:
                 return False
            else:
                 print("CHOOSE A CORRECT OPTION:")
                 print("\n")
                 print("\nwould you like to \n1.Continue\n2.Add another value \n3.Exit")
                 iii=int(input('Your Choice:'))

                 if iii==2:
                    cal.add()
                 elif iii==1:
                      return True
                 elif iii==3:
                    return False

class trignometric():
     def sin(self):
            print("\t\t\t\t\tSINE OPERATION")
            i1=int(input("ENTER A NUMBER 1:"))
            i2=math.radians(i1)
            print("RESULT OF SINE ",i1," VALUE:\t",math.sin(i2))
            print("\nwould you like to \n1.Continue\n2.Add another value \n3.Exit")
            iii=int(input('Your Choice:'))
            if iii==1:
                 return True
            elif iii==2:
                 tri.sin()
            elif iii==3:
                 return False
            else:
                 print("CHOOSE A CORRECT OPTION:")
                 print("\n")
                 print("\nwould you like to \n1.Continue\n2.Add another value \n3.Exit")
                 iii=int(input('Your Choice:'))
                 if iii==1:
                    return True
                 if iii==2:
                    tri.sin()
                 elif iii==3:
                    return False
     def cos(self):
            print("\t\t\t\t\tCOSINE OPERATION")
            i1=int(input("ENTER A NUMBER 1:"))
            i2=math.radians(i1)
            print("RESULT OF COSINE ",i1," VALUE:\t",math.cos(i2))
            print("\nwould you like to \n1.Continue\n2.Add another value \n3.Exit")
            iii=int(input('Your Choice:'))
            if iii==2:
                 tri.cos()
            elif iii==1:
                 return True
            elif iii==3:
                 return False
            else:
                 print("CHOOSE A CORRECT OPTION:")
                 print("\n")
                 print("\nwould you like to \n1.Continue\n2.Add another value \n3.Exit")
                 iii=int(input('Your Choice:'))
                 if iii==2:
                    tri.cos()
                 elif iii==3:
                    return False
                 elif iii==1:
                    return True 
     def tan(self):
            print("\t\t\t\t\tTANGENT OPERATION")
            i1=int(input("ENTER A NUMBER 1:"))
            i2=math.radians(i1)
            print("RESULT OF TANGENT ",i1," VALUE:\t",math.tan(i2))
            print("\nwould you like to \n1.Continue\n2.Add another value \n3.Exit")
            iii=int(input('Your Choice:'))
            if iii==2:
                 tri.tan()
            elif iii==1:
                 return True
            elif iii==3:
                 return False
            else:
                 print("CHOOSE A CORRECT OPTION:")
                 print("\n")
                 print("\nwould you like to \n1.Continue\n2.Add another value \n3.Exit")
                 iii=int(input('Your Choice:'))
                 if iii==2:
                    tri.tan()
                 elif iii==3:
                    return False
                 elif iii==1:
                    return True           
     def cont(self):
            print("\t\t\t\t\tCONTANGENT OPERATION")
            i1=int(input("ENTER A NUMBER 1:"))
            i2=math.radians(i1)
            print("RESULT OF COTANGENT ",i1," VALUE:\t",1/math.tan(i2))
            print("\nwould you like to \n1.Continue\n2.Add another value \n3.Exit")
            iii=int(input('Your Choice:'))
            if iii==2:
                 tri.cont()
            elif iii==1:
                 return True
            elif iii==3:
                 return False
            else:
                 print("CHOOSE A CORRECT OPTION:")
                 print("\n")
                 print("\nwould you like to \n1.Continue\n2.Add another value \n3.Exit")
                 iii=int(input('Your Choice:'))
                 if iii==2:
                    tri.cont()
                 elif iii==3:
                    return False
                 elif iii==1:
                    return True 
    
     def sec(self):
            print("\t\t\t\t\tSECANT OPERATION")
            i1=int(input("ENTER A NUMBER 1:"))
            i2=math.radians(i1)
            print("RESULT OF SECANT ",i1," VALUE:\t",1/math.cos(i2))
            print("\nwould you like to \n1.Continue\n2.Add another value \n3.Exit")
            iii=int(input('Your Choice:'))
            if iii==2:
                 tri.sec()
            elif iii==1:
                 return True
            elif iii==3:
                 return False
            else:
                 print("CHOOSE A CORRECT OPTION:")
                 print("\n")
                 print("\nwould you like to \n1.Continue\n2.Add another value \n3.Exit")
                 iii=int(input('Your Choice:'))
                 if iii==2:
                    tri.sec()
                 elif iii==3:
                    return False
                 elif iii==1:
                    return True 
                 
     def cosec(self):
            print("\t\t\t\t\tCOSECANT OPERATION")
            i1=int(input("ENTER A NUMBER 1:"))
            i2=math.radians(i1)
            print("RESULT OF COSECANT ",i1," VALUE:\t",1/math.sin(i2))
            print("\nwould you like to \n1.Continue\n2.Add another value \n3.Exit")
            iii=int(input('Your Choice:'))
            if iii==2:
                 tri.cosec()
            elif iii==1:
                 return True
            elif iii==3:
                 return False
            else:
                 print("CHOOSE A CORRECT OPTION:")
                 print("\n")
                 print("\nwould you like to \n1.Continue\n2.Add another value \n3.Exit")
                 iii=int(input('Your Choice:'))
                 if iii==2:
                    tri.cosec()
                 elif iii==3:
                    return False
                 elif iii==1:
                    return True 

class so():
     def sqr(self):
          print("\t\t\t\tSQUARE ROOT")
          print("\n")
          iii=int(input("ENTER A NUMBER:"))
          print("SQUARE ROOT OF ",iii,"=",math.sqrt(iii))
          print("\nwould you like to \n1.Continue\n2.Add another value \n3.Exit")
          iii=int(input('Your Choice:'))
          if iii==2:
               sops.sqr()
          elif iii==1:
               return True
          elif iii==3:
               return False
          else:
               print("CHOOSE A CORRECT OPTION:")
               print("\n")
               print("\nwould you like to \n1.Continue\n2.Add another value \n3.Exit")
               iii=int(input('Your Choice:'))
               if iii==2:
                    sops.sqr()
               elif iii==3:
                    return False
               elif iii==1:
                    return True  

     def pw(self):
            print("\t\t\t\t\tPOWER OF N OPERATION")
            i1=int(input("ENTER A NUMBER 1:"))
            i2=int(input("ENTER A POWER OF:"))
            print("THE POWER OF ",i1,"^",i2,"= ",math.pow(i1,i2))
            print("\nwould you like to \n1.Continue\n2.Add another value \n3.Exit")
            iii=int(input('Your Choice:'))
            if iii==2:
                 sops.pw()
            elif iii==3:
                 return False
            elif iii==1:
                 return True
            else:
                 print("CHOOSE A CORRECT OPTION:")
                 print("\n")
                 print("\nwould you like to \n1.Continue\n2.Add another value \n3.Exit")
                 iii=int(input('Your Choice:'))
                 if iii==2:
                    sops.pw()
                 elif iii==1:
                      return True
                 elif iii==3:
                    return False 
     def log(self):
          print("\t\t\t\tLOGARITHM")
          print("\n")
          iii=int(input("ENTER A NUMBER:"))
          print("LOG OF ",iii,"=",math.log(iii))
          print("\nwould you like to \n1.Continue\n2.Add another value \n3.Exit")
          iii=int(input('Your Choice:'))
          if iii==2:
               sops.log()
          elif iii==1:
               return True
          elif iii==3:
               return False
          else:
               print("CHOOSE A CORRECT OPTION:")
               print("\n")
               print("\nwould you like to \n1.Continue\n2.Add another value \n3.Exit")
               iii=int(input('Your Choice:'))
               if iii==2:
                    sops.log()
               elif iii==3:
                    return False
               elif iii==1:
                    return True  

     def fact(self):
          print("\t\t\t\tFACTORIAL OF A NUMBER")
          print("\n")
          iii=int(input("ENTER A NUMBER:"))
          print("FACTORIAL OF ",iii,"=",math.factorial(iii))
          print("\nwould you like to \n1.Continue\n2.Add another value \n3.Exit")
          iii=int(input('Your Choice:'))
          if iii==2:
               sops.fact()
          elif iii==1:
               return True
          elif iii==3:
               return False
          else:
               print("CHOOSE A CORRECT OPTION:")
               print("\n")
               print("\nwould you like to \n1.Continue\n2.Add another value \n3.Exit")
               iii=int(input('Your Choice:'))
               if iii==2:
                    sops.fact()
               elif iii==3:
                    return False
               elif iii==1:
                    return True  
a=True
cal=calculator()
tri=trignometric()
sops=so()
while a:
    print("\r\t\t\t\t\tWELCOME TO THE DM CALCULATOR")
    print("OPERATIONS:")
    print("\n1.ARITHMETIC OPERATIONS\n")
    print("2.TRIGNOMETRIC OPERATIONS\n")
    print("3.SPECIAL OPERATIONS")
    print("\n4.EXIT")
    i=int(input("Your Choice:"))
    if i==1:
        print("\t\t\t\t\tARITHMETIC OPERATION")
        print("\n1.ADDITION")
        print("2.SUBTRACTION")
        print("3.MULTIPLICATION")
        print("4.DIVISION")
        print("5.MODULUS")
        print("6.Exit")
        ii=int(input("Your Choices:"))
        if ii==1:
            a=cal.add()
        elif ii==2:
             a=cal.sub()
        elif ii==3:
             a=cal.mul()
        elif ii==4:
             a=cal.div()
        elif ii==5:
             a=cal.mod()
        elif ii==6:
             break
        else:
             print("CHOOSE A CORRECT OPTION:")
             print("\n")
             continue
    elif i==2:
        print("\t\t\t\t\t\t\tTRIGNOMETROIC OPERATIONS")
        print("\n1.SINE")
        print("\n2.COSINE")       
        print("\n3.TANGENT")
        print("\n4.COTANGENT")
        print("\n5.SECANT")
        print("\n6.COSECANT") 
        print("\n7.EXIT")
        t=int(input("Your Choice:"))
        if t==1:    
            a=tri.sin()
        elif t==2:    
            a=tri.cos()
        elif t==3:    
            a=tri.tan()
        elif t==4:    
            a=tri.cont()
        elif t==5:    
            a=tri.sec()
        elif t==6:    
            a=tri.cosec()
        elif t==7:
             break
        else:
             print("CHOOSE A CORRECT OPTION:")
             print("\n")
             continue           
    elif i==3:
         print("\t\t\t\t\tSPECIAL OPERATIONS")
         print("\n1.SQUARE ROOT")
         print("\n2.POWER OF N")
         print("\n3.LOGARITHM") 
         print("\n4.FACTORIAL") 
         ii=int(input("Your Choice:"))
         if ii==1:
              a=sops.sqr()
         elif ii==2:
              a=sops.pw()
         elif ii==3:
              a=sops.log()
         elif ii==4:
              a=sops.fact()   
          



    

