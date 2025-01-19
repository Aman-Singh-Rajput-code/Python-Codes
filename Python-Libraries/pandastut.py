'started on 13/09/2024'

'''import pandas as pd
print(pd.__version__)'''
#...........................................................................................................................................................................................................
''' 
'series in pandas'
#A pandas series is like a column in a table .it is 1D array which holds data of any type
#Here we will create a simple pandas series
import pandas as pd
aman=[1,7,2]
amannew=pd.Series(aman)
print(amannew)

#laabeling - label can use to access a specified value
import pandas as pd
aman=[1,7,2]
amannew=pd.Series(aman)
print(amannew[0])

#creating our own name label (index)
import pandas as pd
aman=[1,7,2]
amannew=pd.Series(aman,index=['aman','shiwani','choti'])
print(amannew)

#labeling - label can be use to access a specified value (after creating own label)
import pandas as pd
aman=[1,7,2]
amannew=pd.Series(aman,index=['aman','shiwani','choti'])
print(amannew['aman'])

#you can also use a key or value object like a dictionary, when creating a series
#here we will create a simple pandas series from a dictionary
import pandas as pd
cal={'day1':420,'day2':380,'day3':390}
amannew=pd.Series(cal)
print(amannew)

#now we will create a series using only data from day1 and day2
import pandas as pd
cal={'day1':420,'day2':380,'day3':390}
result=pd.Series(cal,index=['day1','day2'])
print(result)

#DataFrame:Data sets in pandas are usually multidimensional table,and they are called DataFrame.
#Series are like column and dataframe is the whole table

#we will now create a dataframe from 2 series
import pandas as pd
aman={'cal':[420,380,590],'duration':[21,45,75]}
amannew=pd.DataFrame(aman)
print(amannew)'''

#........................................................................................................................................................................................................
'''
'DataFrame:it is a  2D data structure like 2D array with table including rows and columns'
#example from last lec
import pandas as pd
data={'cal':[420,380,390],'dur':[50,40,45]}
aman=pd.DataFrame(data)
print(aman)

#Locate row: pandas use the loc attribute to return one or more specified rows
import pandas as pd
data={'cal':[420,380,390],'dur':[50,40,45]}
aman=pd.DataFrame(data)
print(aman.loc[0])

#example of returning row 0 and 1
import pandas as pd
data={'cal':[420,380,390],'dur':[50,40,45]}
aman=pd.DataFrame(data)
print(aman.loc[[0,1]])

#named index : with the index arg,you can name your own index
import pandas as pd
data={'cal':[420,380,390],'dur':[50,40,45]}
aman=pd.DataFrame(data,index=['day1','day2','day3'])
print(aman)

#locate the named index
import pandas as pd
data={'cal':[420,380,390],'dur':[50,40,45]}
aman=pd.DataFrame(data,index=['day1','day2','day3'])
print(aman.loc['day2'])

#output in DataFrame:
import pandas as pd
data={'cal':[420,380,390],'dur':[50,40,45]}
aman=pd.DataFrame(data,index=['day1','day2','day3'])
print(aman.loc[['day1','day2']])'''
#'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
'''
#load the data from the csv file into dataframe i.e Churn_modeling.csv
'read csv files:(comma separated file) it is a simple way to store the big and biggest data sets.csv files contains plain text'

#loading the csv into dataframe with to_string(to_string are used to show all data)
import pandas as pd
fileload = pd.read_csv(r'Churn_Modelling.csv')
print(fileload.to_string())

#loading the csv into dataframe withoutt to_string
import pandas as pd
fileload = pd.read_csv(r'Churn_Modelling.csv')
print(fileload)

#max_rows:you can  check your system's maximumm  rows with 
import pandas as pd
print(pd.options.display.max_rows)  

#yes we can increase maximum  number of rows to display the entire datafraame
import pandas as pd
pd.options.display.max_rows=11000  #to increase no. of rows
df=pd.read_csv(r'Churn_Modelling.csv')
print(df) ''' 

#...........................................................................................................................................................................
'''
#handling Json files 
'JSON: Big data sets are normally stoed and extracted as json.Json is a plain text,but it has a format of ab object'
#loading the JSON into datafame
import pandas as pd
aman=pd.read_json('data.js')   #this file doesn't exist,we have just taken as example
print(aman.to_string())

#Dictionary as a JSON:if your code is not in a file,but in a python dictionary,then you can do all below:
import pandas as pd
data = {
    "Duration":{
        "0":60,
        "1":60,
        "2":60,
        "3":45,
        "4":45,
        "5":60
    },
    "pulse":{
        "0":110,
        "1":117,
        "2":103,
        "3":109,
        "4":117,
        "5":102
    },
    "maxpulse":{
        "0":130,
        "1":145,
        "2":135,
        "3":175,
        "4":148,
        "5":127
    },
    "Calories":{
        "0":409.1,
        "1":479.0,
        "2":340.0,
        "3":282.4,
        "4":406.0,
        "5":300.5
    }
    }
amannew = pd.DataFrame(data)
print(amannew)'''
#.................................................................................................................................................................................
'''
'viewing the data: one of the most used method for a quick overview of the dataframe is the head() method.This method returns the header and a specified number of rows'
#here we will print the 1st 10 rows in the dataframe
import pandas as pd
aman = pd.read_csv('Churn_Modelling.csv')
print(aman.head(10))

#here we will print the lasr 10 rows in the dataframe
import pandas as pd
aman = pd.read_csv('Churn_Modelling.csv')
print(aman.tail(10))

#what if you want the information about the data in the dataframe:via info()
#here we will print the 1st 10 rows in the dataframe
import pandas as pd
df = pd.read_csv('Churn_Modelling.csv')
print(df.info())'''

#...............................................................................................................................................................................................................................

'''
#cleaning data: it means fixing the bad data in your data set. bad data could be:empty cell,
#data in a wrong format,duplicate data and wrong data.
#empity cell:it will give you wrong result always,we will have to rows alweays that contains
#the bad data

#loading and reading the original dataframe
import pandas as pd
aman = pd.read_csv('Car_sales.csv')
print(aman.to_string())

#here we wil return a new data frame with no empty cell
import pandas as pd
aman = pd.read_csv('Car_sales.csv')
amannew = aman.dropna()
print(amannew.to_string())

#if at any case you want to change the original dataframe,than use inplace=true argument.
#it will remove the rows containing the null(NaN) values.
import pandas as pd
aman = pd.read_csv('Car_sales.csv')
aman.dropna(inplace=True)
print(aman.to_string)

#replacing the empty values:we will use the fillna() method which will allow us to replace the empty ceell with a value
import pandas as pd
aman = pd.read_csv('Car_sales.csv')
aman.fillna(130,inplace=True)
print(aman.to_string)

#to replace only the empty value for one column,you need to specify the column name.
import pandas as pd
aman = pd.read_csv('Car_sales.csv')
aman["__year_resale_value"].fillna(130.6,inplace=True)
print(aman.to_string)

#here we can also replace the empty cell using mean(),median() or mode().
#cal the MEAN and replace the empity values with it
import pandas as pd
aman = pd.read_csv('Car_sales.csv')
x = aman["__year_resale_value"].mean()
aman["__year_resale_value"].fillna(x,inplace=True)
print(aman.to_string)

#cal the MEDIAN and replace the empity values with it
import pandas as pd
aman = pd.read_csv('Car_sales.csv')
x = aman["__year_resale_value"].median()
aman["__year_resale_value"].fillna(x,inplace=True)
print(aman.to_string)

#cal the MODE and replace the empity values with it
import pandas as pd
aman = pd.read_csv('Car_sales.csv')
x = aman["__year_resale_value"].mode()[0]
aman["__year_resale_value"].fillna(x,inplace=True)
print(aman.to_string)'''  
#...................................................................................................................................................................................................................................

#Cleanig wrong formate data
'''
#Now let's try to convert all the cell in the date column into date.via to_datetime()
import pandas as pd
data=pd.read_csv('Car_sales.csv')
data["Latest_Launch"]=pd.to_datetime(data["Latest_Launch"])
print(data.to_string())

#now we will remove all the coloumns with NULL values in 'date' coloumn
import pandas as pd
data=pd.read_csv('Car_sales.csv')
data['Latest_Launch']=pd.to_datetime(data['Latest_Launch'])
data.dropna(subset=['Latest_Launch'],inplace=True)
print(data.to_string())
'''
#...................................................................................................................................................................................................................................

#Wrong Data:its only a wrong data
'''
#loading and reading the original dataframe
import pandas as pd
data=pd.read_csv('dirty_dataset.csv')
print(data.to_string())


#Now we will set age=55 and 49 in row 52
import pandas as pd
data=pd.read_csv('dirty_dataset.csv')
print(data.to_string())
for i in data.index:
    if data.loc[i,'Age']>100:
        data.loc[i,'Age']=data.loc[i,'Age']/10
print(data.to_string())

#for larger data set:now here we wil loop through all the values in "Age" column,if the value is higher than 100 then set it to 100
import pandas as pd
data=pd.read_csv('dirty_dataset.csv')
for i in data.index:
    if data.loc[i,'Age']>100:
        data.loc[i,'Age']=100
print(data.to_string())

#You can also remove the rows for wrong data in larger dataset
import pandas as pd
data=pd.read_csv('dirty_dataset.csv')
for i in data.index:
    if data.loc[i,'Age']>100:
        data.drop(i,inplace=True)
print(data.to_string())
'''
#...................................................................................................................................................................................................................

#Removing duplicates values:1st you need to discover the duplicate values via duplicate() method
'''
#loading and reading the original dataframe
import pandas as pd
data=pd.read_csv('dirty_dataset.csv')
print(data.to_string())

#return True for Every row that is duplicate otherwise return false:
import pandas as pd
data=pd.read_csv('dirty_dataset.csv')
dupli=data.duplicated()
print(dupli)

#removing duplicated from the data set. via drop_duplicated()
import pandas as pd
data=pd.read_csv('dirty_dataset.csv')
data.drop_duplicates(inplace=True)
print(data.to_string())
'''
 


