#prime numbers between two number taken from user
a=int(input("enter number 1: "))   #this is first number
b=int(input("enter number 2: "))   #this is second number

for i in range(a,b):
    flag=0   #indicator variable
    for j in range(2,i):
        if i%j==0:
            flag=1
            break
    if flag==0:
        print(i,"prime")  #this prints prime numbers between range
    # else:
    #     print(i,"compposite")      #uncomment this to find composite numbers also
