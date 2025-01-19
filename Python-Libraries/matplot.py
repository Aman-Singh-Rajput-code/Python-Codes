#intro
'''import matplotlib
print(matplotlib.__version__)

#pyplot submodule
#now we will draw a line in a diagram from a certain position 
import matplotlib.pyplot as plt
import numpy as np
x=np.array([0,6])
y=np.array([0,8])
plt.plot(x,y)
plt.show()'''

#......................................................................................................................................................................................................

#details about matplotlib and pyplot
'''import matplotlib.pyplot as plt #now the pyplot package can be refered as plt
import numpy as np
#ploting x and y
#plot() function is used to draw points or maeker in  a diagram
#there are 2 parameters for specifying points in the diagram i.e x-axis and y-axis
x=np.array([1,8])
y=np.array([3,10])
plt.plot(x,y)
plt.show()

#x-axis is horizontal axis
#y-axis is vertical axis

#ploting without line
import matplotlib.pyplot as plt
import numpy as np
x=np.array([1,8])
y=np.array([3,10])
plt.plot(x,y,"o")
plt.show()

#drawing zig zag lines 
import matplotlib.pyplot as plt
import numpy as np
x=np.array([1,8,9,2])
y=np.array([3,7,6,4])
plt.plot(x,y)
plt.show()

#default x-point
#if we do not specify the point x-axis then show default values 0,1,2,3,4,5......
import matplotlib.pyplot as plt
import numpy as np
y=np.array([1,5,2,4])
plt.plot(y)
plt.show()'''

#......................................................................................................................................................................................................

#more about marker(points we plot while drawign),function and designing
'''import matplotlib.pyplot as plt
import numpy as np
y=np.array([1,5,2,4])
plt.plot(y,marker='o')
plt.show()

#line colour and styling
from tkinter import Y
import matplotlib.pyplot as plt
import numpy as np
y=np.array([1,5,2,4])
plt.plot(y,'o:r')
plt.show()

#line refrence
#1] - solid line
#2] : dotted line
#3] -- dashed line
#4] -. dashline/dotted line (combined)

#colour refrence 
#1] r red
#2] g green
#3] b blue
#4] c cylon
#5] m magenta
#6] y yellow
#7] k black
#8] w white

#marker size - ms
import matplotlib.pyplot as plt
import numpy as np
y=np.array([1,4,2,5,6])
plt.plot(y,marker='o',ms=10.5)
plt.show() 

#matker edge colour - mec
import matplotlib.pyplot as plt
import numpy as np
y = np.array([1,4,2,5])
plt.plot(y,marker='o',ms=20,mec='r')
plt.show()

#marker face colour - mfc
import matplotlib.pyplot as plt
import numpy as np
y = np.array([1,4,2,5])
plt.plot(y,marker='o',ms=20,mec='y',mfc='r')    #can use colour like r,y,b... or else can use colour codes 
plt.show()                                      # for example red colour = r = #4CAF50
'''
#......................................................................................................................................................................................................

#linestyle or ls - is used to change the style of ploted line
'''import matplotlib.pyplot as plt
import numpy as np
y=np.array([2,4,6,1,10])
plt.plot(y,ls='dotted') #line reference
plt.show()

#line color - c
import matplotlib.pyplot as plt
import numpy as np
y=np.array([2,4,6,1,10])
plt.plot(y,ls='dotted',color='r')
plt.show()

#line width - lw
import matplotlib.pyplot as plt
import numpy as np
y=np.array([2,4,6,1,10])
plt.plot(y,ls='dotted',lw=20.5)
plt.show()

#example for multiple line
import matplotlib.pyplot as plt
import numpy as np
x = np.array([1,3,5,2,7])
y=np.array([2,4,6,1,10])
plt.plot(x,ls = '--',lw = 5.1,color = 'b')
plt.plot(y,ls='dotted',lw = 6.2,color = 'y')
plt.show()'''

#......................................................................................................................................................................................................

#working on labels of x and y axix as well as header of graph
'''import matplotlib.pyplot as plt
import numpy as np
x = np.array([80,85,90,95,100,105,110,115,120,125])
y = np.array([240,250,260,270,280,290,300,310,320,330])
plt.xlabel('Amount')
plt.ylabel('SIP return')
plt.plot(x,y)
plt.show()

#header of graph
import matplotlib.pyplot as plt
import numpy as np
x = np.array([80,85,90,95,100,105,110,115,120,125])
y = np.array([240,250,260,270,280,290,300,310,320,330])
plt.title('Market analysis')
plt.xlabel('Amount')
plt.ylabel('SIP Return')
plt.plot(x,y)
plt.show()

#setting font property and more about font styling
import matplotlib.pyplot as plt
import numpy as np
x = np.array([80,85,90,95,100,105,110,115,120,125])
y = np.array([240,250,260,270,280,290,300,310,320,330])
font1 = {'family':'serif','size':15.5,'color':'blue'}
font2 = {'family':'serif','size':10.5,'color':'red'}
plt.title('Market analysis',fontdict=font1)
plt.xlabel('Amount',fontdict=font2)
plt.ylabel('SIP Return',fontdict=font2)
plt.plot(x,y)
plt.show()

#can also change location of label and titles using loc()
import matplotlib.pyplot as plt
import numpy as np
x = np.array([80,85,90,95,100,105,110,115,120,125])
y = np.array([240,250,260,270,280,290,300,310,320,330])
font1 = {'family':'serif','size':15.5,'color':'blue'}
font2 = {'family':'serif','size':10.5,'color':'red'}
plt.title('Market analysis',fontdict=font1,loc='left')
plt.xlabel('Amount',fontdict=font2)   #can also change location of x and y axis as well
plt.ylabel('SIP Return',fontdict=font2)
plt.plot(x,y)
plt.show()'''
#......................................................................................................................................................................................................

#more about grid lines
'''import matplotlib.pyplot as plt
import numpy as np
x = np.array([80,85,90,95,100,105,110,115,120,125])
y = np.array([240,250,260,270,280,290,300,310,320,330])
font1 = {'family':'serif','size':15.5,'color':'blue'}
font2 = {'family':'serif','size':10.5,'color':'red'}
plt.title('Market analysis',fontdict=font1)
plt.xlabel('Amount',fontdict=font2)
plt.ylabel('SIP Return',fontdict=font2)
plt.plot(x,y)
plt.grid()
plt.show()

#now we will  specifically design which grid line we want whether on x axis or y axis (defaukt grid val. are on both axis and grid which we draw manually are known as legal values)
import matplotlib.pyplot as plt
import numpy as np
x = np.array([80,85,90,95,100,105,110,115,120,125])
y = np.array([240,250,260,270,280,290,300,310,320,330])
font1 = {'family':'serif','size':15.5,'color':'blue'}
font2 = {'family':'serif','size':10.5,'color':'red'}
plt.title('Market analysis',fontdict=font1)
plt.xlabel('Amount',fontdict=font2)
plt.ylabel('SIP Return',fontdict=font2)
plt.plot(x,y)
plt.grid(axis='x')
plt.show()

#setting up grid properties
import matplotlib.pyplot as plt
import numpy as np
x = np.array([80,85,90,95,100,105,110,115,120,125])
y = np.array([240,250,260,270,280,290,300,310,320,330])
font1 = {'family':'serif','size':15.5,'color':'blue'}
font2 = {'family':'serif','size':10.5,'color':'red'}
plt.title('Market analysis',fontdict=font1)
plt.xlabel('Amount',fontdict=font2)
plt.ylabel('SIP Return',fontdict=font2)
plt.plot(x,y)
plt.grid(axis='x',color = 'green',lw = 0.5)
plt.grid(axis="y",color = 'red',lw = 0.7)
plt.show()'''
#......................................................................................................................................................................................................

#subploting in matplotlb
#display multiple plots  - with subplot() you can draw multiple plots in one figure
'''import matplotlib.pyplot as plt
import numpy as np

#plot1
x = np.array([0,1,2,3])
y = np.array([3,1,8,10])
plt.subplot(1,2,1) #the figure has 1 row,2 column and this plot is the 1plot
plt.plot(x,y)

#plot2
x = np.array([0,1,2,3])
y = np.array([10,20,30,40])
plt.subplot(1,2,2) #the figure has 1 row,2 column and this plot is the 1plot
plt.plot(x,y)

plt.show()

#now we will draw two plot on top of each other
import matplotlib.pyplot as plt
import numpy as np

#plot1
x = np.array([0,1,2,3])
y = np.array([3,1,8,10])
plt.subplot(2,1,1) #the figure has 1 row,2 column and this plot is the 1plot
plt.plot(x,y)

#plot2
x = np.array([0,1,2,3])
y = np.array([10,20,30,40])
plt.subplot(2,1,2) #the figure has 1 row,2 column and this plot is the 1plot
plt.plot(x,y)

plt.show()

#now we wil draw challenge of 6 plot 
import matplotlib.pyplot as plt
import numpy as np

#plot1
x = np.array([0,1,2,3])
y = np.array([3,9,2,10])
plt.subplot(2,3,1)
plt.plot(x,y)
plt.title('sales1')

#plot2
x = np.array([0,1,2,3])
y = np.array([3,9,2,10])
plt.subplot(2,3,2)
plt.plot(x,y)
plt.title('sales2')

#plot3
x = np.array([0,1,2,3])
y = np.array([3,9,2,10])
plt.subplot(2,3,3)
plt.plot(x,y)
plt.title('sales3')

#plot4
x = np.array([0,1,2,3])
y = np.array([3,9,2,10])
plt.subplot(2,3,4)
plt.plot(x,y)
plt.title('sales4')

#plot5
x = np.array([0,1,2,3])
y = np.array([3,9,2,10])
plt.subplot(2,3,5)
plt.plot(x,y)
plt.title('sales5')

#plot6
x = np.array([0,1,2,3])
y = np.array([3,9,2,10])
plt.subplot(2,3,6)
plt.plot(x,y)
plt.title('sales6')

plt.suptitle('MY SHOP') #BY usinbg suptite()= supertitle we can give title to the main header of the graph
plt.show()'''

#......................................................................................................................................................................................................

#Learnign in deap about scater plot 
#scater - the scater() function plot one dot for each observation 
'''import matplotlib.pyplot as plt
import numpy as np
x = np.array([5,7,8,2,4,1,6,9,10,14,11,3,12])
y = np.array([99,86,49,20,94,59,84,52,63,69,43,56,62])
plt.scatter(x,y)
plt.show()

#now we will compare 2 plots on same figure
import matplotlib.pyplot as plt
import numpy as np
#day1,the age and speed of 13 cars
x = np.array([5,7,8,2,4,1,6,9,10,14,11,3,12])
y = np.array([99,86,49,20,94,59,84,52,63,69,43,56,62])
plt.scatter(x,y)
#day2,the age and speed of 13 cars
x = np.array([3,6,9,1,2,4,6,8,5,2,6,7,10])
y = np.array([100,105,90,95,85,69,94,30,96,86,90,70,100])
plt.scatter(x,y)
plt.show()

#now we will set our own color of mrker(blue and orange are bydefault)
import matplotlib.pyplot as plt
import numpy as np
#day1,the age and speed of 13 cars
x = np.array([5,7,8,2,4,1,6,9,10,14,11,3,12])
y = np.array([99,86,49,20,94,59,84,52,63,69,43,56,62])
plt.scatter(x,y,c = 'yellow')
#day2,the age and speed of 13 cars
x = np.array([3,6,9,1,2,4,6,8,5,2,6,7,10])
y = np.array([100,105,90,95,85,69,94,30,96,86,90,70,100])
plt.scatter(x,y,c = 'green')
plt.show()

#Now we will change color of each dot/scatter 
import matplotlib.pyplot as plt
import numpy as np
#day1
x = np.array([5,7,8,2,19,4,5,9,3,11,6,10,13])
y = np.array([69,79,89,96,95,75,86,54,96,88,99,50,100])
colors = (['red','black','green','blue','pink','yellow','orange','gray','purple','brown','cyan','magenta','beige'])
plt.scatter(x,y,color = colors)
plt.show()

#now we will create color array and specify a colormap in scatter plot
import matplotlib.pyplot as plt
import numpy as np
#day1
x = np.array([5,7,8,2,19,4,5,9,3,11,6,10,13])
y = np.array([69,79,89,96,95,75,86,54,96,88,99,50,100])
colors = ([0,10,20,30,40,45,50,55,60,70,80,90,100])
plt.scatter(x,y,c = colors,cmap='viridis')
plt.colorbar()   #this is used to show colorbar in graph
plt.show()

#can also change size of dots
import matplotlib.pyplot as plt
import numpy as np
#day1
x = np.array([5,7,8,2,19,4,5,9,3,11,6,10,13])
y = np.array([69,79,89,96,95,75,86,54,96,88,99,50,100])
sizes = ([10,20,30,10.5,20.5,30.5,200,500,100,150,300,123,50])
plt.scatter(x,y,s = sizes)
plt.show()

#alpha - you can adjust transperancy of dots
import matplotlib.pyplot as plt
import numpy as np
#day1
x = np.array([5,7,8,2,19,4,5,9,3,11,6,10,13])
y = np.array([69,79,89,96,95,75,86,54,96,88,99,50,100])
sizes = ([10,20,30,10.5,20.5,30.5,200,500,100,150,300,123,50])
plt.scatter(x,y,s = sizes,alpha=0.3)
plt.show()

#try to run alpha,color and size function at once
import matplotlib.pyplot as plt
import numpy as np
x = np.random.randint(100,size=(100))
y = np.random.randint(100,size=(100))
color = np.random.randint(100,size=(100))
sizes = 10*np.random.randint(100,size=(100))
plt.scatter(x,y,c = color,s = sizes,alpha=0.5,cmap='nipy_spectral')
plt.colorbar()
plt.show()'''
#......................................................................................................................................................................................................

#Bars in matplotlib
'''#vertical bars
import matplotlib.pyplot as plt
import numpy as np
x = np.array(['A','B','C','D'])
y = np.array([3,8,1,10])
plt.bar(x,y)
plt.show()

#for horizontal section
import matplotlib.pyplot as plt
import numpy as np
x = np.array(['A','B','C','D'])
y = np.array([3,8,1,10])
plt.barh(x,y)
plt.show()

#color of bar() and barh()
import matplotlib.pyplot as plt
import numpy as np
#https://matplotlib.org/stable/gallery/color/named color.html
#https://htmlcolorcodes.com/
x = np.array(['A','B','C','D'])
y = np.array([3,8,1,10])
plt.bar(x,y,color = 'red')
plt.show()

#can change bar width
import matplotlib.pyplot as plt
import numpy as np
x = np.array(['A','B','C','D'])
y = np.array([3,8,1,10])
plt.bar(x,y,width=0.5)  #for horizontal bars use height insted of width (width=height)
plt.show()'''
#......................................................................................................................................................................................................

#Histogram in matplotlib
'''#Histogram- a histogram is a graph showing the frequency distribution
#example - say you ask for the height of 250 people then how we will make histogram
#hist() function is used for histogram
import numpy as np
x = np.random.normal(170,10,250)
print(x)

#hist() function will read the array and produce the hsitogram
import matplotlib.pyplot as plt
import numpy as np
x = np.random.normal(170,10,250)
plt.hist(x)
plt.show()'''
#......................................................................................................................................................................................................

#piechart in matplotlib 
'''#creating the pie chart using pie() function
import matplotlib.pyplot as plt
import numpy as np
y = np.array([35,25,25,15])
plt.pie(y)
plt.show()

#labeling each segment/legend of pie chart
import matplotlib.pyplot as plt
import numpy as np
y = np.array([35,25,25,15])
mylabel = (['Apple','Cherry','Banana','Mango'])
plt.pie(y,labels=mylabel)
plt.show()

#startangle parameter - default start angle is at x-axis to change startangle parameter is used
import matplotlib.pyplot as plt
import numpy as np
y = np.array([35,25,25,15])
mylabel = (['Apple','Cherry','Banana','Mango'])
plt.pie(y,labels=mylabel,startangle=90)
plt.show()

#Exploding piechart by some value
import matplotlib.pyplot as plt
import numpy as np
y = np.array([35,25,25,15])
mylabel = (['Apple','Cherry','Banana','Mango'])
myexplode = ([0.1,0,0,0])
plt.pie(y,labels=mylabel,explode=myexplode)
plt.show()

#using shadow effect 
import matplotlib.pyplot as plt
import numpy as np
y = np.array([35,25,25,15])
mylabel = (['Apple','Cherry','Banana','Mango'])
myexplode = ([0.1,0,0,0])
plt.pie(y,labels=mylabel,explode=myexplode,shadow=True)
plt.show()'''

#specifiying color for each wedge
import matplotlib.pyplot as plt
import numpy as np
y = np.array([35,25,25,15])
mylabel = (['Apple','Cherry','Banana','Mango'])
myexplode = ([0.1,0,0,0])
mycolor = (['red','hotpink','yellow','green'])
plt.pie(y,labels=mylabel,explode=myexplode,shadow=True,colors=mycolor)
plt.legend()   #this used to show index in piechart
plt.show()

#Adding legend with header
import matplotlib.pyplot as plt
import numpy as np
y = np.array([35,25,25,15])
mylabel = (['Apple','Cherry','Banana','Mango'])
myexplode = ([0.1,0,0,0])
mycolor = (['red','hotpink','yellow','green'])
plt.pie(y,labels=mylabel,explode=myexplode,shadow=True,colors=mycolor)
plt.legend(title = "Fruits")   #this used to show index in piechart
plt.show()