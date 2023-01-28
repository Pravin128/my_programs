#check wheaher number is prime or not using user defined function
def prime(): 
    n=int(input("enter number:"))  #for getting input from user
    flag=0
    for i in range(2,n):  #range to divide the number
        if n%i==0:       
            flag=1
            break
    if flag==0:
        print("prime") 
    else:
        print("composite")
prime()   #calling of function
