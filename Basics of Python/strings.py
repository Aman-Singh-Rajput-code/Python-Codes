#basics of strings
#1
name1='aman singh'  
name2="aman singh"  #single and double quote does not allow next line like triple qoute
#name3='''aman
#singh'''
'''print(name1,name2 ,name3)
print(type(name2))
print(len(name1))

#2)indexing
print(name1[0])  #positive indexing 
print(name1[-1])    #negative indexing
print()

#3)traversing uaing for loop
for i in name1:
    print(i)
print()
#4)traversing using list comprehension
lst=[char for char in name1]
for i in lst:
    print(i)
   
#find char/substring in string
print(name1.find('man')) #substring
print(name1.find('s')) #character
print(name1.find('ram')) #if char isn't present in the string then return -1

#slicing of string  name1='aman singh'
print(name1[0:3]) #positive indexing
print(name1[-4:-1]) #negative indexing

#modifieng strings
# 1)upper and lower case
str1="mumbai city"
str2=str1.upper()
print(str2)
str3=str2.lower()
print(str3)
str4=str3.capitalize()
print(str4)
str5="    helloo     "
print(str5.strip())   #for removing unwanted spaces in string
str6="hello world!!, what a beautiful world this is!"
print(str6.replace("world","earth",1))
str7="ram,krishna,shiv,radhe,sia"
list=str7.split(",",1)
print(list)
str8= "jai hind"
print(str7+str8) #concatination
stud="aman"
marks=63
clg='SIESGST'   # for string formating(just like callbyvalue)
str9="the student is {s},and marks is {m},and college is {c}".format(s=stud,m=marks,c=clg)
print(str9)'''
text="the unexpected always happens"
print(text)
print(len(text))
print(text.find("expec"))  #string revice
print(text[:11])
print(text.replace("always",'never'))
text2=" no matter what "
new=text+text2
print(new)