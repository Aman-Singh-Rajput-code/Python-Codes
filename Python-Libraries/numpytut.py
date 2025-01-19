#lec1 numpy intro
'''import numpy as np
print(np.__version__)'''
#.............................................................................................................................................................................................

#lec2 (creating a numpy ndarray(array which are created in numpy))
'''import numpy as np
x=np.array([1,2,3,4,5])  #insted pf list we can also use tuple or any other array like object
print(x)              #with array() it will be convert  into ndarray
print(type(x))'''

#dimension in array - a Dimenssion in array is one level of array depth(nested aray)
# 0-D array - scalar,are the element in an array,each value in an array is 0-D array

#now we will create 0-D array with val 13
'''import numpy as np
x=np.array(13)
print(x)'''

#1-D array :- an array thst has 0-D array as its element is 1-D Array
'''import numpy as np
aman=np.array([1,2,3,4,5])
print(aman)'''

#2-D array :- containing two array with certain val
'''import numpy as np
x=np.array([[1,2,3],[4,5,6]])
print(x)'''

#3-D array with 2-D array
'''import numpy as np
aman=np.array([[[1,2,3],[4,5,6]],[[1,2,3],[4,5,6]]])
print(aman)'''

'''#to check dimensions dimension of array ndim is used
print(aman.ndim)
#to convert dimension of array
import numpy as np
x=np.array([[1,2,3],[4,5,6]],ndmin=5)
print(x)
print(x.ndim)'''
#........................................................................................................................................................................

#array indexing and index concept
''''1-d array'
import numpy as np
arr=np.array([1,2,3,4,5])
print(arr[2])  #for printing perticular element
print(arr[1]+arr[2])       # for adding perticular element

'2-d array'  
import numpy as np
arr=np.array([[1,2,3,4,5],[1,2,3,4,5]])
print("5th element in the 2nd rows ",arr[1,4])  #for printing particular element of required rows

'3-d array'
import numpy as np
arr=np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])
print(arr)
print('3rd element in 3rd row',arr[1,0,2])
'''
#........................................................................................................................................................................................................................................

#slicing of array
'''
'we will slice from 1-5 elements'
import numpy as np
arr=np.array([1,2,3,4,5,6,7,8,9])
print(arr[1:5])

'we will slice from starting to somewhere in the mid'
import numpy as np
arr=np.array([1,2,3,4,5,6,7,8,9])
print(arr[:4])

'we will slice from somewhere in mid till end'
import numpy as np
arr=np.array([1,2,3,4,5,6,7,8,9])
print(arr[4:])

'negative slicing '
import numpy as np
arr=np.array([1,2,3,4,5,6,7,8,9])
print(arr[-6:-1])

'alternative slicing'
import numpy as np
arr=np.array([1,2,3,4,5,6,7,8,9])
print(arr[0::2])

'slicing of 2-d array'
import numpy as np
arr=np.array([[1,2,3,4,5],[6,7,8,9,10]])
print(arr[1,1:4])  #here first arg is for list nd second arg is for indexing

'another ex of 2-d array'
import numpy as np
arr=np.array([[1,2,3,4,5],[6,7,8,9,10]])
print(arr[0:2,1:3])

'3-d array'
import numpy as np
arr=np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])
print(arr[0:2,0:1])'''
#................................................................................................................................................................................................................


#numpy datatypes
'''
i for integer
b for boolean
u for unsigned integer
f for float
c for complex float
m for timedelta
M for datetime
O for object
S for string
U for inicode string
V for memory
'''

#cheacking the datatype of numpy array -dtype
'''import numpy as np
aman=np.array([1,2,3,4])
print(aman.dtype)

#cheacking datatype of numpy array -string
import numpy as np
aman=np.array(['kela','aam','lichi'])
print(aman.dtype)

#cheacking array with defined data type:
import  numpy as np
aman=np.array([1,2,3,4],dtype='S')
print(aman)
print(aman.dtype)

#now we will create an array with data type of 4 byte int:
import numpy as np
aman=np.array([1,2,3,4],dtype='i4')
print(aman)
print(aman.dtype)

#if a type is given in which the elements cannot be casted then numpy will raise error.what if a val cannot be converted
import numpy as np
aman=np.array(['a','2','3'],dtype='i')
print(aman.dtype)

#converting data type in existing array - astype()
import numpy as np
aman=np.array([1.1,2.1,3.1,4.1])
aman1=aman.astype('i')
print(aman1)
print(aman1.dtype)

#converting data type from int to boolean
import numpy as np
aman=np.array([1,0,3])
aman1=aman.astype(bool)
print(aman1)
print(aman1.dtype)
'''
#....................................................................................................................................................................................................................

#diff  btw numpy array and view
#we will make aw copy,change in original array,and display both

'''import numpy as np
aman=np.array([1,2,3,4,5])
aman1=aman.copy()
aman1[0]=12
print(aman)
print(aman1)

#now we will make a view, change original,display both
import numpy as np
aman=np.array([1,2,3,4,5])
aman1=aman.view()
aman[0]=42
print(aman)
print(aman1)'''
#......................................................................................................................................................................................................

#shape of an array- the shape of an array is the number of element inn each dimensions
#now we will try to get the shape of any aaray
'''import numpy as np
aman=np.array([[1,2,3,4],[5,6,7,8]])
print(aman.shape)

#(2,4) which means the arrray has 2 dimensions and it has 4 elements

#now we will create a 5-D array using ndim:
import numpy as np
aman=np.array([1,2,3,4],ndmin=5)
print(aman)
print('shape of array is',aman.shape)
'''
#.................................................................................................................................................................................................

#reshaping - means changing the shape  of an array,like adding or remove the element

#reshaping from 1-D to 2-D
'''import numpy as np
aman=np.array([1,2,3,4,5,6,7,8,9,10,11,12])
aman1=aman.reshape(4,3)
print(aman1)

#reshaping from 1-D to 3-D
import numpy as np
aman=np.array([1,2,3,4,5,6,7,8,9,10,11,12])
aman1=aman.reshape(2,3,2)
print(aman1)

#return copy or view
import numpy as np
aman=np.array([1,2,3,4,5,6,7,8])
print(aman.reshape(2,4).base)

#unkown dimensions - you are only allowed to have one unknown dimension. pass -1
import numpy as np
aman=np.array([1,2,3,4,5,6,7,8])
aman1=aman.reshape(2,2,-1)
print(aman1)

#flattening the array by converting multidimensional array in 1-D
import numpy as np
aman=np.array([[1,2,3],[4,5,6]])
aman1=aman.reshape(-1)
print(aman1)

#there are alot of functioning for changing the shapes of an array in numpy.
#like flatten,revel,fliplr,flipud.they all are actully comes under advance numpy.
'''
#............................................................................................................................................................................................................................

#Iterating array-means going through the elements one by one or step by step.like for lop
'''
#Iterate the element of 1-D
import numpy as np
aman=np.array([1,2,3])
for i in aman:
    print(i)

#Iterate the element of 2-D
import numpy as np
aman=np.array([[1,2,3],[4,5,6]])
for i in aman:
    print(i)

#Iterate the each scalar element of 2-D
import numpy as np
aman=np.array([[1,2,3],[4,5,6]])
for i in aman:
    for a in i:
        print(a)

#Iterate the each scalar element of 3-D
import numpy as np
aman=np.array([[[1,2,3],[4,5,6],[7,8,9],[10,11,12]]])
for i in aman:
    for a in i:
        for b in a:
            print(b)

#Iterating array using the nditer() function
#Now we will Iterate on each scalar element
import numpy as np
aman=np.array([[[1,2],[3,4],[5,6],[7,8]]])
for i in np.nditer(aman):
    print(i)

#now we will Iterate with different step sizes(doubt
import numpy as np
aman=np.array([[1,2,3,4],[5,6,7,8]])
for i in np.nditer(aman[0,1::2]):
    print(i)
'''

#.............................................................................................................................................................................................................
'''
#joining  the numpy array - here for this we will pass concatenate()
import numpy as np
aman=np.array([1,2,3])
aman1=np.array([4,5,6])
aman2=np.concatenate((aman,aman1))
print(aman2)

#joining of 2-D array along with rows(axis=1
import numpy as np
aman=np.array([[1,2],[3,4]])
aman1=np.array([[5,6],[7,8]])
aman2=np.concatenate((aman,aman1),axis=1)
print(aman2)

#joining array using the stack function
import numpy as np
aman=np.array([1,2,3])
aman1=np.array([4,5,6])
aman2=np.stack((aman,aman1),axis=1)
print(aman2)

#stacking along with rows:hstack()
import numpy as np
aman=np.array([1,2,3])
aman1=np.array([4,5,6])
aman2=np.hstack((aman,aman1))
print(aman2)

#stacking along with column
import numpy as np
aman=np.array([1,2,3])
aman1=np.array([4,5,6])
aman2=np.vstack((aman,aman1))
print(aman2)

#stacking along with height(depth)
import numpy as np
aman=np.array([1,2,3])
aman1=np.array([4,5,6])
aman2=np.dstack((aman,aman1))
print(aman2)'''

#.........................................................................................................................................................................................................................................................
'''
#spliting array in numpy-it is reverse to joining,breaking the array
#array_split()

#split the array in 3 parts:
import numpy as np
aman=np.array([1,2,3,4,5,6])
amannew=np.array_split(aman,3)
print(amannew)

#split the array in 4 parts:
import numpy as np
aman=np.array([1,2,3,4,5,6])
amannew=np.array_split(aman,4)
print(amannew)

#spliting into array with index
import numpy as np
aman=np.array([1,2,3,4,5,6])
amannew=np.array_split(aman,3)
print(amannew[0])
print(amannew[1])
print(amannew[2])

#spliting the 2-D array into three 2-D array 
import numpy as np
aman=np.array([[1,2,3],[4,5,6],[7,8,9],[10,11,12],[13,14,15],[16,17,18]])
amannew=np.array_split(aman,3)
print(amannew)

#spliting the 2-D array into three 2-D array along with rows
import numpy as np
aman=np.array([[1,2,3],[4,5,6],[7,8,9],[10,11,12],[13,14,15],[16,17,18]])
amannew=np.array_split(aman,3,axis=1)
print(amannew)

#spliting the 2-D array into three 2-D array along with rows(alternate is using hsplit(),opposite hstack())
import numpy as np
aman=np.array([[1,2,3],[4,5,6],[7,8,9],[10,11,12],[13,14,15],[16,17,18]])
amannew=np.hsplit(aman,3,)
print(amannew)
'''
#............................................................................................................................................................................................................................................
'''
#searching array-you can search an array  for a certain value and return the indexes that get the match,by using where()
import numpy as np
aman=np.array([1,2,3,4,5,4,4])
amannew=np.where(aman==4)
print(amannew)

#now we will find the indexes where the values are even:
import numpy as np
aman=np.array([1,2,3,4,5,6,7,8])
amannew=np.where(aman%2==0)
print(amannew)

#now we will find the indexes where the values are odd:
import numpy as np
aman=np.array([1,2,3,4,5,6,7,8])
amannew=np.where(aman%2==1)
print(amannew)

#searchsorted() - perform binary search in array.
#we will now find the index where the value 7 should be inserted.
import numpy as np
aman=np.array([6,7,8,9])
aman1=np.searchsorted(aman,7)
print(aman1)

#now we will search from right side
import numpy as np
aman=np.array([6,7,8,9])
aman1=np.searchsorted(aman,7,side='right')
print(aman1)

#how we will search multiple values(doubt)
import numpy as np
aman=np.array([1,3,5,7])
aman1=np.searchsorted(aman,[2,4,6])
print(aman1)
'''
#...............................................................................................................................................................................................................................
'''
#sort()-the numpy ndarray object has a function which is called sort(),and this will sort a specified array
import numpy as np
aman=np.array([3,2,0,1])
print(np.sort(aman))  #this method is like the copy

#sort the array alphabetically
import numpy as np
aman=np.array(['shiwani','aman','choti'])
print(np.sort(aman))

#sort the boolean array
import numpy as np
aman=np.array([True,False,True])
print(np.sort(aman))

#sorting 2-D array
import numpy as np
aman=np.array([[3,2,4],[5,0,1]])
print(np.sort(aman))
'''

'completed on 13/09,2024'