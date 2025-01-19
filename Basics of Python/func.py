'''# to add numbers using diffrent methods of func.
def add(n1,n2):  # defining a function
    sum=n1+n2
    return sum
x=2
y=3   
print("the sum is :",add(x,y))  # default argument
print("the sum is :",add(n1=4,n2=5))   # keyword\named argument
print("the sum is :",add(2,4))  # positinal argument

def sumnum(*args):
    sum=0
    for i in args:
        sum+=i
    return sum
output = sumnum(1,2,3,4,5,6)  # arbitary argument (variabl-len argument)
print("sum is :", output)


def stud(**kwargs):
    for x,y in kwargs.items():    #keyword\kwargs argument
        print(x,"is",y)
    print()      
stud(name="aman",age=19,city='mumbai')
stud(name="raj",age=11,city='pune')
stud(name="dj",age=20,city="jaunpur")


#nested function
def outer():
    x=1
    def inner():
        y=2
        result=x+y
        return result
    return inner()
output=outer()
print(output) '''


#pass by value(mutable)
def addone(x):
    x=x+1
    print("in to the function: ",x)

x=5         #here function take value as per defined
addone(x)   #here funtion do mot imapct on main 
print("outside function :",x)

#pass by refrence(unmutable)
def modifylist(lst):
    lst.append(4)
    #lst=[5,6,7]
    print("inside function:",lst)

lst=[1,2,3]  #here function take value from function
modifylist(lst)     # here function impact the main
print("outsde function :",lst)
