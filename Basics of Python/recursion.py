#factorial using recursion
'''def fact(n):
    if n==0:
        return 1
    ans=n*fact(n-1)
    return ans
n=int(input("enter the no. :"))
print((fact(n)))'''

#print num from n to 1 and 1 to n
'''def nto1(n):
    if n==0:
        return 
    #n=int(input("enter number :")) 
    #print(n)
    nto1(n-1)
    print(n)
nto1(5)'''

# sum from 1 to n
'''def add(n):
    if n==1:
        return 1
    sum=n+add(n-1)
    return sum
n=int(input("enter the no. :"))
print(add(n))'''

#a raise to power b
'''def pow(a,b):
    if b==0:
        return 1
    ans=a*pow(a,b-1)
    return ans
a=int(input("enter a: "))
b=int(input("enter b: "))
print(pow(a,b))'''

#fibonacci series in resursion
def fibonacci(n):
    if n==1:
        return 0
    elif n==2:
        return 1
    else:
        return (fibonacci(n-1) + fibonacci(n-2))
n=int(input("enter no. : "))
for i in range(1,n+1):
    print(fibonacci(i)) 