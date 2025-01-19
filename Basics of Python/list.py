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
