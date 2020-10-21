n = int(input("enter a number for operations : "))
def sum1():
    list=[]
    n1 = int(input("Enter the number for sum : "))
    for i in range(n1):
        e=int(input("enter elementS for sum : "))
        list.append(e)
    print("sum = ",sum(list))

  

def minus():
    a = int(input("enter 1st number for minus : "))
    a1 = int(input("enter 2nd number for minus : "))
    print("Subtraction : ",a-a1)
   

def mul():
    list=[]
    n1 = int(input("Enter the number for multiplication operation : "))
    for i in range(n1):
        e=int(input("enter elements for multiply : "))
        list.append(e)
    res=1
    for x in list:
        res=res*x
    print("multiplication : ",res)


def div():
    a = int(input("enter 1st  number for divide : "))
    a1 = int(input("enter 2nd number for divide : "))
    print("division : ",a/a1)


while(n>=0):
    x = input("enter a symbol (+ ,-,*,/) for operation and press (exit) for exit : ")
    if(x == '+'):
        sum1()
    elif(x=='-'):
        minus()
    elif(x=='*'):
        mul()
    elif(x=='/'):
        div()
    elif(x=='exit'):
        exit()
    
    n=n-1