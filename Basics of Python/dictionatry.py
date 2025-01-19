'''phone={"john":985647,
       "vansh":85236974,    # to create a dictionary
       "anand":824815}
print(phone)
print(type(phone))
print(len(phone))
print(phone["john"])      # to get a perticular eleement of the dic.
print(phone.keys())
phone["john"]=44548515      # to update the dic.
print(phone)
phones={"rahul":12356}  
phone.update(phones)        # to add another dic. to existing dic.
print(phone)
phone.pop("rahul")             # to pop elements(pop()=to remove last element )
print(phone)
#phone.clear()  # to clr dic.
#print(phone)
for _ in phone:
    print(phone)
for x,y in phone.items():
    print(x,y)

dict={
    'a':100,
    'b':200,
    'c':300
}
print( "the sum of dic is: ",sum (dict.values()))   # for getting values of keys
'''

