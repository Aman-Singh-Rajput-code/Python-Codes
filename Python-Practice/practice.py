#num is pos or neg
'''n=int(input("enter the number: "))
if n>=0:
    print('number is positive')
else:
    print('number is negative')'''

# find num is even or odd
'''n=int(input("enter the number: "))
if n%2 == 0 :
    print("the number is even ")
else:
    print("the number is odd ")'''

#find loss or profit
'''c_p=int(input("enter the cost price of product: "))
s_p=int(input("enter the selling price of the product: "))
if c_p>s_p:
    print("seller incurred loss")
    loss=c_p-s_p
    print("loss of ruppes:",loss)
elif c_p<s_p:
    print("seller incurred profit")
    profit=s_p-c_p
    print("profit of ruppes:",profit)
else:
    print("seller has no profit and no loss")'''

#grading system
'''marks=int(input("enter the marks: "))
if (marks>80 & marks<=100):
    print("very good")
elif(marks>60 & marks<=80):
    print("good")
elif(marks>40 & marks<=60):
    print("average")
else:
    print("failed")'''

#greatest no.
'''num1=int(input("enter num1: "))
num2=int(input("enter num2: "))
num3=int(input("enter num3: "))
if num1>num2:
    if num1>num3:
        print("num1 is greatest")
    else:
        print("num3 is gratest")
else:
    if num2>num3:
        print("num2 is greatest")
    else:
        print("num3 is greatest")'''

#match case
'''num1=int(input("enter num1: "))
num2=int(input("enter num2: "))
option=input("enter options")
match option:
    case"+":
        print("sum is ",num1+num2)
    case"-":
        print("diff is ",num1-num2)
    case"*" : 
        print("mul is ", num1*num2)       
    case"/":
        print("div is ", num1/num2)
    case"_":
        print("invalid choice")'''

# odd or even using ternary operator
'''num=int(input("enter number : "))
output="even" if num%2==0 else "odd"
print("output is : ",output)'''

#element of list using for loop
#for l in range(1,11,1):
 #   print(l)

#patterns(*****)
'''n = int(input("enter num:"))
for _ in range(n):
    print("*"*10)'''    


'''n = int(input("enter num:"))
for i in range (1,n+1):   # for rows
    for j in range (1,n+1):  #for coloumns
        print(j,end="") #end is a keyword to keep them in same line
    print()'''   

'''n = int(input("enter num:"))
for i in range(1,n+1):
    for j in range(1,i+1):
        print(j,end=" ")
    print()'''

'''n = int(input("enter num:"))
for i in range(1,n+1):
    print(" "*(n-i),end="")
    for j in range(1,2*i):
        print(j,end="")
    print()'''

#basics of list
'''a=[5,4,1,2,3]
#a[2]="mango"
#print(a)
#print(a[0:5])   # to get a perticular set from list
#print(a[-2]) #for negative indexing
#print(type(a))
#print(len(a))
a.append("tired")  # to add element in the last of list
print(a)
a.insert(2,"men")  #to add element to a perticular index
print(a)
b=['aman','singh','rajput']
a.extend(b)   #to add another list
print(a)
a.remove("tired")  #to remove element
print(a)
a.pop()  #if index is mentioned then that element will be get popped
print(a)
a[4:6]=[7,8]  #to update a set of list
print(a)'''

'''#sorting of list
a=[1,4,5,2,3,6,7]
print("unsorted list is :",a)
a.sort() # ascending sorting
print("sorted list is :",a)
a.reverse()
print(a) #for deceending sorting'''

#comprehension of list (making new list from existin list)
'''a=[10,30,[40,20,50],70,60,80]
b=[a for a in a if a>=40]  # for getting perticular element from list acc. to coondition
print(b)
c=a.copy()  #for coping list
print(c)
b=b+a  
print(b)

print(a[2])
print(a[2][0])    #nested list

temp=a[2]
a[2]=a[5]
a[5]=temp  #for swapimg elements 
print(a)'''

# [tuples 
# same as list]


'''# for list and set (common elemnets from three list)
l1=[1,2,3,4,5]
l2=[5,6,7]
l3=[5,8,9]
s1=set(l1)
s2=set(l2)
s3=set(l3)
a=s1.intersection(s2)
b=a.intersection(s3)
final_list=list(b)
print(final_list)'''

'''#get mirror string 
input_string=input("enter the string:")
n=int(input(" enter n: "))
alpha="abcdefghijklmnopqrstuvwxyz"
rev=alpha[::-1] # to rev a list\string\etc
#bprint(rev)
dict=dict(zip(alpha,rev))  #to join to dic.
pref=input_string[0:n-1]
suff=input_string[n-1:]
mirror="" 
for i in range(0,len(suff)):
    mirror=mirror+dict[suff[i]]  #to add mirror char to string
res=pref=mirror
print("the result is : ", res)'''


#wap for palindrome or not
str=input("enter your string :")
print(str)
n=len(str)
print(n)
def pali():
    s=str[::-1]
    return s
print(pali())
if pali()==str:
    print("true")
else:
    print("false")
